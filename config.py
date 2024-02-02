import os

API_ID = API_ID = 21386395

API_HASH = os.environ.get("API_HASH", "d8058892a71f31cede948eb24cefdae7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6508232811:AAFkf8VZZ_PiJgQL_A6daplWbWBCtb_P0n4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1297798209))

LOG = -1002057238629

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1311808931").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


