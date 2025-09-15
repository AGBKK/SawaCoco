#!/usr/bin/env python3
"""
SawaCoco MCT Oil Telegram Bot - Main Entry Point
Automated content posting bot for MCT Oil products
"""

import asyncio
import logging
import signal
import sys
from telegram_bot import TelegramContentBot

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class BotManager:
    def __init__(self):
        self.bot = None
        self.running = False

    async def start(self):
        """Start the bot with proper error handling"""
        try:
            self.bot = TelegramContentBot()
            self.running = True
            
            # Start the bot
            success = await self.bot.start_bot()
            
            if not success:
                logger.error("Failed to start bot")
                return False
            
            # Keep running
            logger.info("Bot is now running. Press Ctrl+C to stop.")
            while self.running:
                await asyncio.sleep(1)
                
        except KeyboardInterrupt:
            logger.info("Received shutdown signal")
            await self.shutdown()
        except Exception as e:
            logger.error(f"Bot crashed: {e}")
            await self.shutdown()
            return False
        
        return True

    async def shutdown(self):
        """Graceful shutdown"""
        logger.info("Shutting down bot...")
        self.running = False

    def handle_signal(self, signum, frame):
        """Handle system signals"""
        logger.info(f"Received signal {signum}")
        self.running = False

async def main():
    """Main entry point"""
    manager = BotManager()
    
    # Setup signal handlers
    signal.signal(signal.SIGINT, manager.handle_signal)
    signal.signal(signal.SIGTERM, manager.handle_signal)
    
    # Start the bot
    await manager.start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)
