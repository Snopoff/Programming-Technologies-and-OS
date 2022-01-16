# Домашнее задание №2. Docker.
Написать систему на docker-compose и (3 dockerfiles), реализующие набор задач.

Чтобы запустить систему, нужно вызвать ``docker-compose up --build && docker-compose rm -fsv``. Файл, который заполняет БД, называется ``data.csv``. Чтобы передать свои параметры окружения, можно вмето ``docker-compose up`` вызвать ``ENV_VAR=value docker-compose up``. 

Чтобы вызвалось удаление контейнеров, достаточно в нужный момент прервать исполнение команды ``docker-compose up`` путем ``Ctrl+C``.

Список переменных окружения:
 - ``MYSQL_HOST``
 - ``MYSQL_USER``
 - ``MYSQL_PASSWORD``
 - ``MYSQL_ROOT_PASSWORD``
 - ``MYSQL_DATABASE``

Менял код с учетом того, что писалось в беседе в последние часы, поэтому немного не успел к мягкому дедлайну :worried:
