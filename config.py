#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6995809246:AAHuaZKNUcHN1IKzMtfqqb4IqNSttOEyA5o")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "17765492"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "88682d63aba6c3036eda72a70924b577")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001611860340"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "1046893783"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Leo:Loki@cluster0.mskg6xh.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001691572400"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>HELLO {first}</b>\n\n<b>I Am A File Share Bot Only Works For @TamilMoviesDawOfficial</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>HELLO {first}</b>\n\n<b>You Need To Join In My Channel To Use Me 🥲\n\nKindly Please Join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌ 𝖸𝗈𝗎 𝖠𝗋𝖾 𝖭𝗈𝗍 𝖠𝗎𝗍𝗁𝗈𝗋𝗂𝗌𝖾𝖽 𝖴𝗌𝖾𝗋"

ADMINS.append(OWNER_ID)
ADMINS.append(1046893783)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
