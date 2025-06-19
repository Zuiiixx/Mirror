import os
import json

# REQUIRED CONFIG
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))
TELEGRAM_API = int(os.environ.get("TELEGRAM_API", "0"))
TELEGRAM_HASH = os.environ.get("TELEGRAM_HASH", "")
DATABASE_URL = os.environ.get("DATABASE_URL", "")

# OPTIONAL CONFIG
DEFAULT_LANG = os.environ.get("DEFAULT_LANG", "en")
TG_PROXY = json.loads(os.environ.get("TG_PROXY", "{}"))
USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "")
CMD_SUFFIX = os.environ.get("CMD_SUFFIX", "")
AUTHORIZED_CHATS = os.environ.get("AUTHORIZED_CHATS", "")
SUDO_USERS = os.environ.get("SUDO_USERS", "")
STATUS_LIMIT = int(os.environ.get("STATUS_LIMIT", "10"))
DEFAULT_UPLOAD = os.environ.get("DEFAULT_UPLOAD", "rc")
STATUS_UPDATE_INTERVAL = int(os.environ.get("STATUS_UPDATE_INTERVAL", "15"))
FILELION_API = os.environ.get("FILELION_API", "")
STREAMWISH_API = os.environ.get("STREAMWISH_API", "")
EXCLUDED_EXTENSIONS = os.environ.get("EXCLUDED_EXTENSIONS", "")
INCOMPLETE_TASK_NOTIFIER = os.environ.get("INCOMPLETE_TASK_NOTIFIER", "False") == "True"
YT_DLP_OPTIONS = os.environ.get("YT_DLP_OPTIONS", "")
USE_SERVICE_ACCOUNTS = os.environ.get("USE_SERVICE_ACCOUNTS", "False") == "True"
NAME_SWAP = os.environ.get("NAME_SWAP", "")
FFMPEG_CMDS = json.loads(os.environ.get("FFMPEG_CMDS", "{}"))
UPLOAD_PATHS = json.loads(os.environ.get("UPLOAD_PATHS", "{}"))

# Custom Bot Header
CUSTOM_BOT_HEADER = os.environ.get("CUSTOM_BOT_HEADER", "Beast")
CUSTOM_BOT_HEADER_LINK = os.environ.get("CUSTOM_BOT_HEADER_LINK", "https://t.me/MirrorBeast")

# Hyper Tg Downloader
HELPER_TOKENS = os.environ.get("HELPER_TOKENS", "")

# MegaAPI
MEGA_EMAIL = os.environ.get("MEGA_EMAIL", "")
MEGA_PASSWORD = os.environ.get("MEGA_PASSWORD", "")

# Disable Options
DISABLE_TORRENTS = os.environ.get("DISABLE_TORRENTS", "False") == "True"
DISABLE_LEECH = os.environ.get("DISABLE_LEECH", "False") == "True"
DISABLE_BULK = os.environ.get("DISABLE_BULK", "False") == "True"
DISABLE_MULTI = os.environ.get("DISABLE_MULTI", "False") == "True"
DISABLE_SEED = os.environ.get("DISABLE_SEED", "False") == "True"
DISABLE_FF_MODE = os.environ.get("DISABLE_FF_MODE", "False") == "True"

# Telegraph
AUTHOR_NAME = os.environ.get("AUTHOR_NAME", "Beast")
AUTHOR_URL = os.environ.get("AUTHOR_URL", "https://t.me/MirrorBeast")

# Task Limits
DIRECT_LIMIT = int(os.environ.get("DIRECT_LIMIT", "0"))
MEGA_LIMIT = int(os.environ.get("MEGA_LIMIT", "0"))
TORRENT_LIMIT = int(os.environ.get("TORRENT_LIMIT", "0"))
GD_DL_LIMIT = int(os.environ.get("GD_DL_LIMIT", "0"))
RC_DL_LIMIT = int(os.environ.get("RC_DL_LIMIT", "0"))
CLONE_LIMIT = int(os.environ.get("CLONE_LIMIT", "0"))
JD_LIMIT = int(os.environ.get("JD_LIMIT", "0"))
NZB_LIMIT = int(os.environ.get("NZB_LIMIT", "0"))
YTDLP_LIMIT = int(os.environ.get("YTDLP_LIMIT", "0"))
PLAYLIST_LIMIT = int(os.environ.get("PLAYLIST_LIMIT", "0"))
LEECH_LIMIT = int(os.environ.get("LEECH_LIMIT", "0"))
EXTRACT_LIMIT = int(os.environ.get("EXTRACT_LIMIT", "0"))
ARCHIVE_LIMIT = int(os.environ.get("ARCHIVE_LIMIT", "0"))
STORAGE_LIMIT = int(os.environ.get("STORAGE_LIMIT", "0"))

# Insta video downloader
INSTADL_API = os.environ.get("INSTADL_API", "")

# Nzb search
HYDRA_IP = os.environ.get("HYDRA_IP", "")
HYDRA_API_KEY = os.environ.get("HYDRA_API_KEY", "")

# Media Search
IMDB_TEMPLATE = os.environ.get("IMDB_TEMPLATE", """<b>🎬 Title:</b> <a href="{url}">{title}</a> <b>({year})</b>
<b>🎭 Also Known As:</b> <i>{aka}</i>
<b>⭐ Rating:</b> <i>{rating}/10</i>
<b>📅 Release Date:</b> <a href="{url_releaseinfo}">{release_date}</a>
<b>📚 Genre:</b> {genres}
<b>🗣️ Language:</b> {languages}
<b>🌍 Country:</b> {countries}

<b>📖 Storyline:</b>
<code>{plot}</code>

<b>🔗 Explore More:</b> <a href="{url_cast}">Full Cast & Details</a> | <a href="{url}">IMDb Page</a>""")

# Task Tools
FORCE_SUB_IDS = os.environ.get("FORCE_SUB_IDS", "")
MEDIA_STORE = os.environ.get("MEDIA_STORE", "True") == "True"
DELETE_LINKS = os.environ.get("DELETE_LINKS", "False") == "True"
CLEAN_LOG_MSG = os.environ.get("CLEAN_LOG_MSG", "False") == "True"

# Limiters
BOT_MAX_TASKS = int(os.environ.get("BOT_MAX_TASKS", "0"))
USER_MAX_TASKS = int(os.environ.get("USER_MAX_TASKS", "0"))
USER_TIME_INTERVAL = int(os.environ.get("USER_TIME_INTERVAL", "0"))
VERIFY_TIMEOUT = int(os.environ.get("VERIFY_TIMEOUT", "0"))
LOGIN_PASS = os.environ.get("LOGIN_PASS", "")

# Bot Settings
BOT_PM = os.environ.get("BOT_PM", "False") == "True"
SET_COMMANDS = os.environ.get("SET_COMMANDS", "True") == "True"
TIMEZONE = os.environ.get("TIMEZONE", "Asia/Kolkata")

# GDrive Tools
GDRIVE_ID = os.environ.get("GDRIVE_ID", "")
GD_DESP = os.environ.get("GD_DESP", "Uploaded by Beast")
IS_TEAM_DRIVE = os.environ.get("IS_TEAM_DRIVE", "False") == "True"
STOP_DUPLICATE = os.environ.get("STOP_DUPLICATE", "False") == "True"
INDEX_URL = os.environ.get("INDEX_URL", "")

# Rclone
RCLONE_PATH = os.environ.get("RCLONE_PATH", "")
RCLONE_FLAGS = os.environ.get("RCLONE_FLAGS", "")
RCLONE_SERVE_URL = os.environ.get("RCLONE_SERVE_URL", "")
RCLONE_SERVE_PORT = int(os.environ.get("RCLONE_SERVE_PORT", "0"))
RCLONE_SERVE_USER = os.environ.get("RCLONE_SERVE_USER", "")
RCLONE_SERVE_PASS = os.environ.get("RCLONE_SERVE_PASS", "")
SHOW_CLOUD_LINK = os.environ.get("SHOW_CLOUD_LINK", "False") == "True"

# JDownloader
JD_EMAIL = os.environ.get("JD_EMAIL", "")
JD_PASS = os.environ.get("JD_PASS", "")

# Sabnzbd
USENET_SERVERS = json.loads(os.environ.get("USENET_SERVERS", "[]"))

# Update
UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = os.environ.get("UPSTREAM_BRANCH", "master")
UPDATE_PKGS = os.environ.get("UPDATE_PKGS", "True") == "True"

# Leech
LEECH_SPLIT_SIZE = int(os.environ.get("LEECH_SPLIT_SIZE", "0"))
AS_DOCUMENT = os.environ.get("AS_DOCUMENT", "False") == "True"
EQUAL_SPLITS = os.environ.get("EQUAL_SPLITS", "False") == "True"
MEDIA_GROUP = os.environ.get("MEDIA_GROUP", "False") == "True"
USER_TRANSMISSION = os.environ.get("USER_TRANSMISSION", "True") == "True"
HYBRID_LEECH = os.environ.get("HYBRID_LEECH", "True") == "True"
LEECH_PREFIX = os.environ.get("LEECH_PREFIX", "")
LEECH_SUFFIX = os.environ.get("LEECH_SUFFIX", "")
LEECH_FONT = os.environ.get("LEECH_FONT", "")
LEECH_CAPTION = os.environ.get("LEECH_CAPTION", "")
THUMBNAIL_LAYOUT = os.environ.get("THUMBNAIL_LAYOUT", "")

# Log Channels
LEECH_DUMP_CHAT = os.environ.get("LEECH_DUMP_CHAT", "")
LINKS_LOG_ID = os.environ.get("LINKS_LOG_ID", "")
MIRROR_LOG_ID = os.environ.get("MIRROR_LOG_ID", "")

# qBittorrent/Aria2c
TORRENT_TIMEOUT = int(os.environ.get("TORRENT_TIMEOUT", "0"))
BASE_URL = os.environ.get("BASE_URL", "")
BASE_URL_PORT = int(os.environ.get("BASE_URL_PORT", "0"))
WEB_PINCODE = os.environ.get("WEB_PINCODE", "True") == "True"

# Queueing system
QUEUE_ALL = int(os.environ.get("QUEUE_ALL", "0"))
QUEUE_DOWNLOAD = int(os.environ.get("QUEUE_DOWNLOAD", "0"))
QUEUE_UPLOAD = int(os.environ.get("QUEUE_UPLOAD", "0"))

# RSS
RSS_DELAY = int(os.environ.get("RSS_DELAY", "600"))
RSS_CHAT = os.environ.get("RSS_CHAT", "")
RSS_SIZE_LIMIT = int(os.environ.get("RSS_SIZE_LIMIT", "0"))

# Torrent Search
SEARCH_API_LINK = os.environ.get("SEARCH_API_LINK", "")
SEARCH_LIMIT = int(os.environ.get("SEARCH_LIMIT", "0"))
SEARCH_PLUGINS = json.loads(os.environ.get("SEARCH_PLUGINS", "[]"))