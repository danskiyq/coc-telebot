FROM python:3
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD src/bot.py /
ADD src/decorator.py /
ADD me.session /
ADD ybot.session /

CMD [ "python3", "./bot.py" ]
