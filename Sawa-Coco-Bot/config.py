import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Telegram Configuration
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    TELEGRAM_CHANNEL_ID = os.getenv('TELEGRAM_CHANNEL_ID')
    
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    
    # Company Information
    COMPANY_NAME = os.getenv('COMPANY_NAME', 'Sawa Coco')
    MAIN_PRODUCT = os.getenv('MAIN_PRODUCT', 'MCT Oils, MCT Powders & Coconut Shell Charcoal')
    WEBSITE_URL = os.getenv('WEBSITE_URL', 'https://www.sawa-coco.com')
    COMPANY_LOCATION = os.getenv('COMPANY_LOCATION', 'Thailand')
    COMPANY_FOCUS = os.getenv('COMPANY_FOCUS', 'B2B bulk supplier for brands, labs & manufacturers')
    
    # Posting Configuration
    POSTING_HOURS = os.getenv('POSTING_HOURS', '10:15,17:30').split(',')
    TIMEZONE = os.getenv('TIMEZONE', 'UTC')
    POSTS_PER_DAY = int(os.getenv('POSTS_PER_DAY', '4'))
    
    # Content Settings
    CONTENT_VARIETY = os.getenv('CONTENT_VARIETY', 'high')
    
    @classmethod
    def validate_config(cls):
        """Validate that all required configuration is present"""
        required_vars = [
            'TELEGRAM_BOT_TOKEN',
            'TELEGRAM_CHANNEL_ID',
            'OPENAI_API_KEY'
        ]
        
        missing_vars = []
        for var in required_vars:
            if not getattr(cls, var):
                missing_vars.append(var)
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
        return True
