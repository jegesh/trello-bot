# Please, copy this file into config.py and fill in the options below.
import os

TELEGRAM_KEY = os.environ.get('TELEGRAM_BOT_TOKEN', '')
TRELLO_KEY = os.environ.get('TRELLO_KEY', '')

DB_FILE = 'bot.sqlite'
LOG_FILE = 'bot.log'
# DEBUG, INFO, WARNING, ERROR or CRITICAL
LOG_LEVEL = 'WARNING'

TRELLO_WH_HOST = os.environ.get('WEBHOOK_HOST_URL', '')
TRELLO_WH_PORT = 9099

# In seconds
NOTIFICATION_LAG = 5
