# SawaCoco MCT Oil Telegram Bot

Automated Telegram bot for posting engaging content about MCT Oil products, health benefits, and wellness tips.

## 🚀 Quick Setup Guide

### 1. Create Telegram Bot

1. **Message @BotFather on Telegram**
2. **Send `/newbot`**
3. **Choose a name**: `SawaCoco MCT Oil Bot`
4. **Choose a username**: `sawacoco_mct_bot` (must end with 'bot')
5. **Save the token** you receive

### 2. Create Telegram Channel

1. **Create a new channel** in Telegram
2. **Make it public** with username like `@sawacoco_mct`
3. **Add your bot as admin** with posting permissions
4. **Note the channel username** (with @)

### 3. Get OpenAI API Key

1. **Visit**: https://platform.openai.com/api-keys
2. **Create new API key**
3. **Copy and save** the key securely

### 4. Configure Environment

1. **Copy `.env.example` to `.env`**:
   ```bash
   cp .env.example .env
   ```

2. **Edit `.env` with your values**:
   ```env
   TELEGRAM_BOT_TOKEN=your_bot_token_from_botfather
   TELEGRAM_CHANNEL_ID=@your_channel_username
   OPENAI_API_KEY=your_openai_api_key
   COMPANY_NAME=SawaCoco
   MAIN_PRODUCT=MCT Oil
   WEBSITE_URL=https://your-website.com
   ```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Test Locally

```bash
python main.py
```

## 🌐 Deploy to Railway (Recommended - $5/month)

### Why Railway?
- **24/7 uptime** guaranteed
- **$5/month** hobby plan
- **Auto-scaling** and monitoring
- **Easy deployment** from GitHub

### Deployment Steps

1. **Create Railway account**: https://railway.app
2. **Connect your GitHub** repository
3. **Create new project** from GitHub repo
4. **Add environment variables** in Railway dashboard:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHANNEL_ID` 
   - `OPENAI_API_KEY`
   - `COMPANY_NAME`
   - `MAIN_PRODUCT`
   - `WEBSITE_URL`
5. **Deploy** - Railway will automatically detect Python and use `railway.json`

## 📊 Cost Breakdown

| Service | Monthly Cost | Purpose |
|---------|-------------|---------|
| Railway Hosting | $5 | 24/7 bot hosting |
| OpenAI API | $2-5 | Content generation |
| **Total** | **$7-10** | Complete solution |

## 🎯 Features

### Content Types Generated
- **Health Benefits** - MCT Oil advantages
- **Usage Tips** - How to use effectively  
- **Science Facts** - Research-backed information
- **Recipes** - MCT Oil incorporation ideas
- **Fitness Performance** - Athletic benefits
- **Weight Management** - Metabolism support
- **Brain Health** - Cognitive benefits
- **Energy Boost** - Natural energy source
- **Keto Diet** - Low-carb lifestyle support
- **Product Features** - Quality highlights

### Posting Schedule
- **Default**: 4 posts/day at 9:00, 13:00, 17:00, 21:00
- **Customizable** via environment variables
- **Variety ensured** - no repeated topics same day

### Smart Features
- **Fallback content** if OpenAI API fails
- **Automatic hashtags** generation
- **Company branding** on every post
- **Error logging** and recovery
- **Connection testing** before posting

## 🛠 Alternative Hosting Options

### Free Options (Limited)
- **Heroku Free Tier** (discontinued)
- **Replit** - May sleep after inactivity
- **PythonAnywhere** - Limited free hours

### Paid Alternatives
- **DigitalOcean Droplet** - $6/month
- **AWS EC2 t2.micro** - ~$8/month
- **Google Cloud Run** - Pay per use (~$3-8/month)

## 📱 Manual Controls

### Test the Bot
```python
# In Python console
from telegram_bot import TelegramContentBot
import asyncio

bot = TelegramContentBot()
asyncio.run(bot.send_test_post())
```

### Manual Post
```python
# Send specific content type
asyncio.run(bot.manual_post(topic="health_benefits", post_type="educational"))
```

## 🔧 Customization

### Add New Content Topics
Edit `content_generator.py`:
```python
self.content_topics = [
    "your_new_topic",
    # ... existing topics
]
```

### Change Posting Schedule
Edit `.env`:
```env
POSTING_HOURS=6,12,18,22  # 4 times daily
POSTS_PER_DAY=4
```

### Modify Content Style
Update prompts in `ContentGenerator._create_prompt()` method.

## 📈 Monitoring

### Logs
- **Local**: Check console output
- **Railway**: View logs in dashboard
- **File**: `bot.log` contains all activity

### Health Checks
- Bot tests connection on startup
- Sends test post to verify permissions
- Logs all posting attempts

## 🆘 Troubleshooting

### Common Issues

**Bot can't post to channel**:
- Ensure bot is admin in channel
- Check channel username format (@channelname)
- Verify bot has posting permissions

**OpenAI API errors**:
- Check API key validity
- Monitor usage limits
- Fallback content will be used

**Railway deployment fails**:
- Verify all environment variables set
- Check `requirements.txt` format
- Review deployment logs

### Support
- Check `bot.log` for detailed error messages
- Test locally before deploying
- Verify all API keys and tokens

## 📋 Next Steps

1. **Set up accounts** (Telegram, OpenAI, Railway)
2. **Configure environment** variables
3. **Test locally** to ensure everything works
4. **Deploy to Railway** for 24/7 operation
5. **Monitor performance** and adjust content as needed

Your MCT Oil bot will automatically post engaging, varied content about your products 4 times daily, helping build audience engagement and drive sales!
