import os

API_ID = API_ID = 24147139

API_HASH = os.environ.get("API_HASH", "17f525f59de52108805a65f5ffd909e4")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6841462459:AAF6O_r-rJ3Gixl-4ZlHnzlxL-B_5HLSlpw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5935537622))

LOG = -1002146213576

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6971380203").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
