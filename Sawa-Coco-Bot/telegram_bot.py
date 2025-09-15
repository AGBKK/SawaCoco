import asyncio
import logging
from datetime import datetime, time
from telegram import Bot
from telegram.error import TelegramError
from content_generator import ContentGenerator
from config import Config
import schedule
import time as time_module
import threading

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class TelegramContentBot:
    def __init__(self):
        Config.validate_config()
        self.bot = Bot(token=Config.TELEGRAM_BOT_TOKEN)
        self.channel_id = Config.TELEGRAM_CHANNEL_ID
        self.content_generator = ContentGenerator()
        self.posting_times = Config.POSTING_HOURS
        self.posts_per_day = Config.POSTS_PER_DAY
        
    async def send_post(self, content: str) -> bool:
        """Send a post to the Telegram channel"""
        try:
            await self.bot.send_message(
                chat_id=self.channel_id,
                text=content,
                parse_mode='HTML',
                disable_web_page_preview=False
            )
            logger.info(f"Successfully sent post to {self.channel_id}")
            return True
            
        except TelegramError as e:
            logger.error(f"Failed to send post: {e}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error sending post: {e}")
            return False

    async def send_scheduled_post(self):
        """Generate and send a scheduled post"""
        logger.info("Generating scheduled post...")
        
        try:
            # Generate content
            post_data = self.content_generator.generate_post_content()
            content = post_data['content']
            
            # Send the post
            success = await self.send_post(content)
            
            if success:
                logger.info(f"Posted content about: {post_data['topic']} ({post_data['post_type']})")
            else:
                logger.error("Failed to send scheduled post")
                
        except Exception as e:
            logger.error(f"Error in scheduled posting: {e}")

    def schedule_posts(self):
        """Schedule posts for specific times"""
        logger.info(f"Scheduling posts for times: {self.posting_times}")
        
        for time_str in self.posting_times:
            schedule.every().day.at(time_str).do(
                lambda: asyncio.create_task(self.send_scheduled_post())
            )
            logger.info(f"Scheduled post for {time_str}")

    async def test_connection(self) -> bool:
        """Test bot connection and permissions"""
        try:
            bot_info = await self.bot.get_me()
            logger.info(f"Bot connected successfully: @{bot_info.username}")
            
            # Test channel access
            try:
                chat_info = await self.bot.get_chat(self.channel_id)
                logger.info(f"Channel access confirmed: {chat_info.title}")
                return True
            except TelegramError as e:
                logger.error(f"Cannot access channel {self.channel_id}: {e}")
                return False
                
        except TelegramError as e:
            logger.error(f"Bot connection failed: {e}")
            return False

    async def send_test_post(self):
        """Send a test post to verify everything works"""
        test_content = """🧪 **Test Post - @sawacoco_bot is LIVE!**

This is a test message to verify the bot is working correctly!

🥥 Our premium coconut-based products from Thailand:
✅ MCT Oils (60/40 & C8/98) for energy & brain health
✅ MCT Powder for easy mixing in beverages
✅ Coconut Shell Charcoal for BBQ, shisha & industrial use
✅ 100% palm-free, sustainable, chemical-free production

#MCTOil #CoconutCharcoal #SawaCoco #Thailand #TestPost

🥥 Sawa Coco - MCT Oils, MCT Powders & Coconut Shell Charcoal
🌍 Sustainable sourcing from Thailand
https://www.sawa-coco.com"""

        success = await self.send_post(test_content)
        if success:
            logger.info("Test post sent successfully!")
        return success

    def run_scheduler(self):
        """Run the scheduler in a separate thread"""
        while True:
            schedule.run_pending()
            time_module.sleep(60)  # Check every minute

    async def start_bot(self):
        """Start the bot and begin scheduled posting"""
        logger.info("Starting SawaCoco MCT Oil Telegram Bot...")
        
        # Test connection
        if not await self.test_connection():
            logger.error("Bot startup failed - connection test failed")
            return False
        
        # Send test post
        logger.info("Sending test post...")
        await self.send_test_post()
        
        # Schedule posts
        self.schedule_posts()
        
        # Start scheduler in background thread
        scheduler_thread = threading.Thread(target=self.run_scheduler, daemon=True)
        scheduler_thread.start()
        
        logger.info("Bot started successfully! Scheduled posting is now active.")
        logger.info(f"Posts will be sent at: {self.posting_times}")
        
        return True

    async def manual_post(self, topic: str = None, post_type: str = None):
        """Manually trigger a post with optional topic/type"""
        logger.info(f"Manual post requested - Topic: {topic}, Type: {post_type}")
        
        post_data = self.content_generator.generate_post_content(topic, post_type)
        success = await self.send_post(post_data['content'])
        
        if success:
            logger.info(f"Manual post sent successfully: {post_data['topic']} ({post_data['post_type']})")
        
        return success

# Async wrapper for schedule
def async_job(coro):
    """Wrapper to run async functions with schedule"""
    def wrapper():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(coro)
        loop.close()
    return wrapper

if __name__ == "__main__":
    bot = TelegramContentBot()
    
    # Run the bot
    try:
        asyncio.run(bot.start_bot())
        
        # Keep the main thread alive
        while True:
            time_module.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Bot crashed: {e}")
