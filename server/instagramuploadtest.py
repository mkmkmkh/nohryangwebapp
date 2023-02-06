
from instabot import Bot

bot = Bot()

bot.login(username="nohryangbob",
          password="zx031263")

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("mega.jpg",
                 caption="골들볼 메가점 오늘 메뉴")
