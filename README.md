# Trello Bot for Telegram

Simple Telegram bot, notifying users and groups about changes on boards.

Please, notice that __I do not host this bot__ for public use. If you want to
use it—please, clone the sources and host it yourself or find another hoster.

## Installation

This bot was developed with Python 3.5, though it may work on earlier versions.

1. Install the dependencies:

  ```
  pip install -r requirements.txt
  ```

2. Make sure you set the proper values for the following environment variables: `TELEGRAM_BOT_TOKEN`, `TRELLO_KEY`, and `WEBHOOK_HOST_URL`.  Alternatively, you can just fill them in the proper places in the config.py file.

3. Make sure you have created your bot at [@BotFather](https://telegram.me/BotFather) to fill in the _Telegram API key_.

4. You can grab your _Trello API key_ at https://trello.com/app-key.

5. Run the bot with:

  ```
  ./main.py
  ```

That's it. Now you're able to communicate with your bot.

## Running with Docker

`docker build -t trello-bot .`
`docker run -p 9099:9099 trello-bot -d`

Make sure to fill in the missing environment variables in the Dockerfile before attempting to build.

## Translation

Currently this bot only speaks English. If you want to translate it, feel free to modify `bot/messages.py` - every word the bot ever says is listed in there.  A Russian translation is available in the original repository.
