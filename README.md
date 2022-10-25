# Gek Academy    [![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)

> Интерактивная платформа по обучению математических наук, подобие duolingo.
> Важно достигнуть эффекта 'игры' и соперничества, а также мотивации, по средству разных психологических подходов в обучении.

> Версия: 0.3.0

![image](https://i.postimg.cc/nc9f2m3q/gekko.jpg)

#### Цели: 

- Восстановление навыков django, django-orm, drf
- Восстановление навыков javascript (reactjs)
- Обучение новым технологиям и подходам

## Настройки `config/settings`

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Commit коды

    A1 - App core
    A2 - App users
    A3 - App lessons

## Модели

![image](https://i.postimg.cc/TYnWKCZs/gekacademy-models.png)

## API

![image](https://i.postimg.cc/P5QhcF71/gekacademy-api.png)

### Type checks

Running type checks with mypy:

    $ mypy gekacademy

### Тестовое покрытие

Команды для запуска тестов, проверки покрытия unit-тестамы, генерация HTML-отчета:

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

### Тестирование

    $ pytest
    $ pytest -s (with i/o logging)

Тест отдельного модуля    

    $ pytest /tests/test_models.py
    
Тест только с декоратором `@pytest.mark.slow`

    $ pytest -v -m slow

Инверсия предыдущей команды - исключить тесты с декоратором `@pytest.mark.slow`)
    
    $ pytest -v -m "not slow" 

### Celery

Команды запускать только из корня проекта

#### Запустить воркера:

    $ celery -A config.celery_app worker -l info

### Email Server

В разработке используется эмуляция  smtp сервера [MailHog](https://github.com/mailhog/MailHog) с интерфейсом докер контейнера.

Контейнер mailhog-а стартует автоматически со всеми остальными контейнерами.

При тестировании авторизации, сообщения о подтверждении e-mail отправляются в `http://127.0.0.1:8025`

### Sentry

Sentry is an error logging aggregator service. You can sign up for a free account at <https://sentry.io/signup/?code=cookiecutter> or download and host it yourself.
The system is set up with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.

## HTTPS
Сертификаты и ключи хранятся в `certs/*`

#### Генерации локального сертификата (не подтвержденного)

    $ openssl req -x509 -out localhost.crt -keyout localhost.key -newkey rsa:2048 -nodes -sha256 -subj "/CN=localhost"

### Для windows

#### Установить [chocolatey](https://chocolatey.org/install)

    $ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
    
    $ choco 

#### Установить [mkcert](https://github.com/FiloSottile/mkcert)

    $ choco install mkcert
    
    $ mkcert -install
    $ mkcert -key-file gekacademy.local.key -cert-file gekacademy.local.crt localhost 127.0.0.1 ::1 gekacademy.local

#### Обновить windows hosts file

     127.0.0.1 .gekacademy.local

### [Инструкции по подключению сертификата c docker](https://cookiecutter-django.readthedocs.io/en/latest/developing-locally-docker.html#developing-locally-with-https)
    

## Deployment

**Инструкции по деплою**

### Docker

See detailed [cookiecutter-django Docker documentation](http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html).

#### Команды

    $ docker-compose -f local.yml build

    $ docker-compose -f local.yml up

    $ set(export) COMPOSE_FILE=local.yml  (задать путь к докер конфигу)
    $ docker-compose up
    $ docker-compose up -d  (detached-daemon)

#### Вызов команды внутри контейнера

    $ docker-compose -f local.yml run --rm django python manage.py migrate
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    $ docker-compose -f local.yml run --rm django pip install

#### Ребилд

    $ docker-compose -f local.yml up --build

#### Bash

    $ docker-compose -f local.yml run django bash
    $ docker-compose -f local.yml exec django bash
    $ exit
