class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 1842427  # integer value, dont use ""
    API_HASH = "eb8bfaf26cd3ef11991b7768d1533ed0"
    TOKEN = "1741323461:AAHRalpVlkEEkG-Y_GgGzivxrpxY4sfFzdo"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1194553296  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "ShrayanshSharma"
    SUPPORT_CHAT = "Coffee_Support"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001234328262
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001234328262
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://Coffee:#mrinalini1968@database-1.csi6xvs8jxsy.us-east-2.rds.amazonaws.com:5432/dbname"  # needed for any database modules
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = ""  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "SOJPD4HT4E8TQTFZ"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "DQHFT9MN8W09"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "SOJPD4HT4E8TQTFZ"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "64394220e6bd9ba18ad761924060799268c3517f7c5ec83e21537a7a8810eec05d4fede82ee24418044c3553ccc5925152622be97584cfb6e2d9f9e9d380d4dd"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
