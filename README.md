# HTTP-сервер с Nginx reverse-proxy

Проект демонстрирует работу двух контейнеров Docker:
- **Backend** – Python-сервер на `http.server`, отвечающий на `/` текстом `"Hello from Effective Mobile!"`.
- **Nginx** – reverse-proxy, принимает запросы на порту 80 и перенаправляет их на бэкенд.

## Структура проекта
├── backend/
│ ├── Dockerfile
│ └── app.py
├── nginx/
│ ├── Dockerfile
│ └── nginx.conf
├── docker-compose.yml
├── .env
└── README.md

## Требования

- Docker
- Docker Compose

## Запуск

1. Склонировать репозиторий или создать файлы по структуре выше.

2. Настроить порты в файле `.env`:
    ```env
    NGINX_PORT=80
    BACKEND_PORT=8080
3. Запустить проект:
    docker-compose up --build
## Проверка

Выполнить запрос:
curl http://localhost:80

Ожидаемый ответ:
Hello from Effective Mobile!

## Описание архитектуры

 1. Nginx слушает порт, указанный в .env (по умолчанию 80), и принимает входящие запросы.

 2. В конфигурационном файле nginx/nginx.conf определён upstream backend, который указывает на контейнер backend (имя сервиса в Docker Compose) и порт 8080.

 3. Все запросы к корневому пути / проксируются на этот upstream с помощью proxy_pass.

 4. Backend обрабатывает запрос и возвращает строку "Hello from Effective Mobile!".

Таким образом, клиент взаимодействует только с Nginx, а Nginx прозрачно проксирует трафик к внутреннему сервису.

## Безопасность

 1. Backend-приложение запускается от непривилегированного пользователя appuser (не root).

 2. Nginx по умолчанию работает от пользователя nginx (не root).

 3. Backend не публикует порты наружу, доступен только внутри сети Docker.

