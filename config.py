from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "8670b598fef377e6782429b1f664dce6")
      API_ID = int(getenv("API_ID", "5587539"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7220934809:AAHw1khuYmMv3ZcLTB2w4rBB60Dkm529ewY")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1002115868104:-1001903472174").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
