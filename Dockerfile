FROM python:3.6-alpine

RUN adduser -D master

WORKDIR /home/poetflask

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY migrations migrations
COPY poetflask.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP poetflask.py

RUN chown -R poetflask:poetflask ./
USER master

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]