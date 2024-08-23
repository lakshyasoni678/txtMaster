import os

API_ID = API_ID = 29640188

API_HASH = os.environ.get("API_HASH", "e470abc84a3bc445997ee4ea5be87deb")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7466296444:AAFEldR0DXNBmRPBQrNki1zUJEiVbdjDRr8")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7504263874))

LOG = -1002162241025

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7504263874").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
