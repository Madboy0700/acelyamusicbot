import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID", "24054192"))
API_HASH = getenv("API_HASH", "ed9a8a61a1b4a1ad0915cbe87ba490ed")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN", "7090522217:AAEtZU2nkvhhe8vJx4KCZfjorEe5d77XnPc")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://madboy123:madboy0707@madboy07.r1nef.mongodb.net/?retryWrites=true&w=majority&appName=madboy07")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 960))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "5400")
)
# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", "-1002182187594"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", "7669188252"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", #ticaret
    "https://t.me/AcelyaTicaret", 
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AcelyaDuyuru") #duyuru
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GeceExpress") #gurup

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)

# Time after which you're assistant account will leave chats automatically.

AUTO_LEAVE_ASSISTANT_TIME = int(

    getenv("ASSISTANT_LEAVE_TIME", "3400")

)  # Remember to give value in Seconds

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2041df9cbcd142cba804578a2cf85939")

SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "80ffd296320e49299830e80b11e3bf73")

# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 314572800))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 3221225472))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "BAFlvasAVLN0mUDU1C0zDMdgb8eYwKHg5aFpx-agvcYrlaUaVT8UseOES0YETKqHCkWVC45fyf_QFigekDbEDqAI4O16MakoA6Bg6-rkS7nFEeev5ly86xTLo30syloK1oHjchjHuZDh-zOChWtXur-iCaUkaFE4V-0FOAKmaE3CZcgJ_VZXXFm5qBM2-KYtYthkZdcvpNd7aeeZKCdOeyoXA7oKrlmxD6w5VkDHEd1O5B_yGCrHGx61pvhkXGVZ92hTDQlVJ2M1nwbDDo2oqbU7tCltn-faJgvbgFRHxsBfYVbu0dAvl267jxJI3J8ZyjYgdHGlyIKdR8XnCD4uCLpoJp3EjwAAAAHK81kqAA")

STRING2 = getenv("STRING_SESSION2", "BAFvCbAAQ1v0fCv5kXnHqUXS3carfCNEf6zayUkpgx0kPv3ofeQh091MjBPz9Xmu99AftgCXU5wE2q2ClfGK9KgITejhWcK1E6bEB6CoYuZNVwAMbm-xgOrwHAkcvM6qqkyLqI-a9VIQn2_tf6tvwBKbuOQEYxeAioIdBhUtF_RhW8UsYBs4e7_IJ_RLNv5QR4fNSd5qSg4H4q_apXKyrefGGUka9716_IYYzXXKO9FALW3YO1BHdldBpas4n0quq1XFmOUJ6n7LKEtqWuZV3NoyPM_-TDCNDUhSZZE2iptmqB4cCHkwwyWIeWSOYvryJM7L0yJXJKCNPppGJ6cwApWsa1d9jgAAAAHJhZCBAA")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
)
PLAYLIST_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
STATS_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
TELEGRAM_AUDIO_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
TELEGRAM_VIDEO_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
STREAM_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
SOUNCLOUD_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
YOUTUBE_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
SPOTIFY_ARTIST_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
SPOTIFY_ALBUM_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"
SPOTIFY_PLAYLIST_IMG_URL = "https://pbs.twimg.com/media/Ge-AdVWXoAAgz7g?format=jpg&name=900x900"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))



if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
