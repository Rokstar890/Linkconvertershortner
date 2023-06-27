# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "21114403"))
API_HASH = os.environ.get("API_HASH", "192c2b697e9f45650354fd47292ccf78")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5870227633:AAEi2mNjiaWuo0vYRta-XHEQ4zhhMKJI1CI")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("6201745002")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "telegramms")
DATABASE_URL = os.getenv("DATABASE_URL", "Mongodb url") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "5864846606")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1255023013)

#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001646129271")) 

# For Force Subscription
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "ziplinker_net")

# true if forward should be avoided
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True")

# image when someone hit /start
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '')
LINK_BYPASS = "False"
