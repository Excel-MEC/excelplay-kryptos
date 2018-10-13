#!/bin/bash

python excelplay-kryptos/excelplay_kryptos/manage.py makemigrations && \
	python excelplay-kryptos/excelplay_kryptos/manage.py migrate
gunicorn excelplay-kryptos/excelplay_kryptos/excelplay_kryptos.wsgi --bind 0.0.0.0:8001
