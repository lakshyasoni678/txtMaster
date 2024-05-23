import os

API_ID = API_ID = 24147139

API_HASH = os.environ.get("API_HASH", "4b11dd648188731fb7c9bc8083e8791c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7078804290:AAEOgiUjc9tzMte1SBepRZII6cRizz6Bysg")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6594402123))

LOG = -1002079896558

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5186250641").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
