# FROM python:3.6
FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir -p /excelplay/excelplay_kryptos
 WORKDIR /excelplay/excelplay_kryptos
 ADD requirements.txt /excelplay/excelplay_kryptos
 RUN pip install -r requirements.txt
 RUN pip install git+git://github.com/traintraveler/redis-leaderboard.git@5dc215cfe88281401a0f646655b799d02b594e6a
 ADD . /excelplay/excelplay_kryptos
