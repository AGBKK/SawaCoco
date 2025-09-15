#!/bin/bash

# SawaCoco MCT Oil Bot - Deployment Script
# This script helps deploy the bot to Railway

echo "🚀 SawaCoco MCT Oil Bot - Railway Deployment"
echo "============================================="

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ Error: .env file not found!"
    echo "Please copy .env.example to .env and configure your API keys"
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - SawaCoco MCT Oil Bot"
fi

echo "✅ Repository ready for deployment"
echo ""
echo "Next steps:"
echo "1. Push to GitHub:"
echo "   git remote add origin https://github.com/yourusername/sawacoco-telegram-bot.git"
echo "   git push -u origin main"
echo ""
echo "2. Deploy to Railway:"
echo "   - Visit https://railway.app"
echo "   - Create new project from GitHub repo"
echo "   - Add environment variables from your .env file"
echo "   - Deploy!"
echo ""
echo "3. Environment variables to add in Railway:"
echo "   - TELEGRAM_BOT_TOKEN"
echo "   - TELEGRAM_CHANNEL_ID"
echo "   - OPENAI_API_KEY"
echo "   - COMPANY_NAME"
echo "   - MAIN_PRODUCT"
echo "   - WEBSITE_URL"
echo ""
echo "💰 Expected monthly cost: $7-10 (Railway $5 + OpenAI $2-5)"
