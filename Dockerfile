FROM python:3.5

RUN apt-get update
RUN mkdir /bot
ADD . /bot
WORKDIR /bot

RUN pip install -r requirements.txt

ENV TELEGRAM_BOT_TOKEN=
ENV TRELLO_KEY=
ENV WEBHOOK_HOST_URL=

EXPOSE 9099


CMD python main.py
