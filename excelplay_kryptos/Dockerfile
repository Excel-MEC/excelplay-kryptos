FROM kennethreitz/pipenv as build
FROM python:3.6
 ENV PYTHONUNBUFFERED 1
 RUN mkdir -p /excelplay/excelplay_kryptos
 WORKDIR /excelplay/excelplay_kryptos
 ADD Pipfile /excelplay/excelplay_kryptos/
 ADD Pipfile.lock /excelplay/excelplay_kryptos/
 RUN pipenv install 
 ADD . /excelplay/excelplay_kryptos
