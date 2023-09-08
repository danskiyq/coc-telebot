FROM python:3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY src/bot /src/bot
ADD me.session /
ADD ybot.session /

CMD [ "python3", "src/bot/app.py" ]
