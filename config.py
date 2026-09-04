from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "id")
      API_ID = int(getenv("API_ID", "c"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "8787011529:AAE-SzzP2THVjnaZziyHuUpaWS7KxQDUn0Y")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
