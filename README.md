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

6. Authorize the bot to communicate with the Trello API:
  ```
  /auth
  ```
  And follow the instructions the bot gives you.

7. Setup the webhook:
  1. Send a POST request to this url:
  `https://api.trello.com/1/tokens/<auth token from previous step>/webhooks/` with the following request parameters:
   - key=<your trello app key> (received at https://trello.com/app-key)
   - callbackURL=<your server url>:9099/webhook_update/<your chat id>
   - description=<write anything>
   - idModel=<Trello id of object to receive notifications from> (not clear if this is actually necessary)

8. Add any boards you wish to receive notifications from, using the `/notify` command in the conversation with your bot.

That's it. Now test out the bot by making a change in one of the boards you activated via the `/notify` command.

Logs can be viewed in the `bot.log` file that will be created in the root directory of the project.

### How to Obtain Your Telegram Chat ID
1. Start a conversation with your new bot. Say anything, it really doesn’t matter what.
2. Navigate to https://api.telegram.org/bot<bot token>/getUpdates?offset=0
3. If you don’t see JSON output of the conversation, you may need to send the bot another message and refresh the page.
4. From the conversation output, copy the message::from::id field
If this doesn't work, you're on your own...

### How to Get a Model ID From a Trello object
1. Open the info window (side panel) in the desired Trello board.  
2. Copy the link at the bottom of the panel and paste it in a browser, with '.json' appended to the end of it.  
3. In the raw JSON output, the first `"id": ...` you see is the id of the board.  
4. If you look through the output, you can find ID's for all of the objects contained in that board.

## Running with Docker

`docker build -t trello-bot .`
`docker run -p 9099:9099 --net=host trello-bot -d`

Make sure to fill in the missing environment variables in the Dockerfile before attempting to build.

## Translation

Currently this bot only speaks English. If you want to translate it, feel free to modify `bot/messages.py` - every word the bot ever says is listed in there.  A Russian translation is available in the original repository.
