# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "21159773"))
API_HASH = os.environ.get("API_HASH", "49ae08543a07335e195756eba2f56e11")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6242676954:AAHYNKPiCcXF-3tAl7LYO_aH3qIzOqwWzJk")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("5886772061")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Aaroha")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Aaroha9:Aaroha999@cluster0.jqqzc5t.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5886772061")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(5886772061)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001581944173")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "TGshortener") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
