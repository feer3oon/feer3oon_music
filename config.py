import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID","25727878"))
API_HASH = getenv("API_HASH","1d56a0bf20fee0c1a2a925faa17fecf9")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN","6534136166:AAER4svByB-fd6ExFXbzy08nUoNvEG4MCwk")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://Elkber:Elkber@cluster0.feuljpn.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 480))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID","-1002072384730"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6308685423))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/AnonymousX1025/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/source_fer3on")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/zzxxue")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION","BAHI1AwAXwEBeW9XG1Jv2ZdcP2t1DMrM_ZGSSBIdja1ZslGZrJhJ7Dgjd3smF_DRWrCtPccwkwEkK_Cot1OED2y3IPt-orJNfrjVnjxuV1j1WV10dIp8kDxEbi-dwkGqKROtSiZuxTTVJY-Op1TtrtMaK3l54uqVtDnlESeue45oGmEVlijXiqBcpGXafqN6ingX-oQqMGh578zd8T3hOZ0rRCwZm5rDRVmZDSXSeAFiBt7n0vslXUm-f-K5Q0uMz_ZjpZ_IX8VT2wlKQkcIvn4kZRJHltw6vYhkYzz9iGEvwvwASC_8j83EkvY9dyvA2wJSK2kwU4NhBQFtfAdxh3udPkcdEQAAAAF4BuZvAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://te.legra.ph/file/49f06c74aa91d6a2ec9c4.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://te.legra.ph/file/b8a0c1a00db3e57522b53.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/28fbc4e76afb906193e58.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/5786818555c2c8676cb5d.png"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/18a57090040d717742169.png"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/18a57090040d717742169.png"
STREAM_IMG_URL = "https://te.legra.ph/file/237ad27bb053ac874e970.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/237ad27bb053ac874e970.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/98cc55864499abc63ef71.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/98cc55864499abc63ef71.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/98cc55864499abc63ef71.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


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
