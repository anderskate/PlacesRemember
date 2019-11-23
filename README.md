# Places Remember

[![Coverage Status](https://coveralls.io/repos/github/anderskate/PlacesRemember/badge.svg?branch=master)](https://coveralls.io/github/anderskate/PlacesRemember?branch=master)
[![Build Status](https://travis-ci.org/anderskate/PlacesRemember.svg?branch=master)](https://travis-ci.org/anderskate/PlacesRemember)

Веб-приложение, с помощью которого люди могут хранить свои впечатления о посещенных местах.

![scrin](https://user-images.githubusercontent.com/46349173/68991025-eb4e5380-087b-11ea-93d6-a13a9e8fa9e8.png)

## Запуск

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- В приложении используется база данных PostgreSQL с PostGIS. Для правильной работы приложения, нужно установить
геопространственные библиотеки. Подробнее, по ссылке на документацию Django: https://bit.ly/2rIhrfY
- Перенесите миграции в БД командой `python3 manage.py migrate`
- Запустите сервер командой `python3 manage.py runserver` и перейдите по ссылке `http://localhost:8000/admin/`
- Для авторизации пользователей с помощью API Facebook, нужно создать приложение на сайте "Facebook для разработчиков", по ссылке: https://developers.facebook.com/. После создания приложения, нужно его добавить в интерфейс "Django admin", по вкладке "Social applications".

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Необходимо добавить переменные в таком формате: `ПЕРЕМЕННАЯ=значение`.

Доступны 3 переменные:
- `DEBUG` — дебаг-режим. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
- `SECRET_KEY` — секретный ключ проекта
- `DATABASE_URL` — путь до базы данных, формат: `postgres://USER:PASSWORD@HOST:PORT/NAME`
