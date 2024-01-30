# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "24003416"))
API_HASH = os.environ.get("API_HASH", "013d9b3fe388308ff1272d33d1e40e2b")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6858627899:AAEtsmzG_9kRpwXqkULMXn56Bn5K5fTp4fU")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6683865620")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "telegramms")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://pispibordu:Rokstar321@cluster0.roeprbx.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "6683865620")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6683865620)
SHORTNER_LINK = os.environ.get("SHORTNER_LINK", "linksmoney.in")
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002133531200")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "linksmoneyofficial")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://telegra.ph/file/a60660ceaeb7f4a31cdfc.jpg')
LINK_BYPASS = "False"
