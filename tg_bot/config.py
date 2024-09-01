import os

# Create a new config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    API_KEY = os.getenv('API_KEY')
    OWNER_ID = os.getenv('OWNER_ID')
    OWNER_USERNAME = os.getenv('OWNER_USERNAME')

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

    MESSAGE_DUMP = os.getenv('MESSAGE_DUMP')
    LOAD = eval(os.getenv('LOAD'))  # Use eval cautiously
    NO_LOAD = eval(os.getenv('NO_LOAD'))  # Use eval cautiously
    WEBHOOK = os.getenv('WEBHOOK') == 'True'
    URL = os.getenv('URL')
    SUDO_USERS = eval(os.getenv('SUDO_USERS'))  # Use eval cautiously
    SUPPORT_USERS = eval(os.getenv('SUPPORT_USERS'))  # Use eval cautiously
    WHITELIST_USERS = eval(os.getenv('WHITELIST_USERS'))  # Use eval cautiously
    DONATION_LINK = os.getenv('DONATION_LINK')
    CERT_PATH = os.getenv('CERT_PATH')
    PORT = int(os.getenv('PORT'))
    DEL_CMDS = os.getenv('DEL_CMDS') == 'True'
    STRICT_GBAN = os.getenv('STRICT_GBAN') == 'True'
    WORKERS = int(os.getenv('WORKERS'))
    BAN_STICKER = os.getenv('BAN_STICKER')
    ALLOW_EXCL = os.getenv('ALLOW_EXCL') == 'True'
    BMERNU_SCUT_SRELFTI = int(os.getenv('BMERNU_SCUT_SRELFTI'))


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
