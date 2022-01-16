# Домашнее задание №1. Linux & Tmux.
Написать программу, которая запускает в tmux N изолированных окружений (директорий) Jupyter.

Скрипт ```hw1.py``` -- нужная программа. 

Запуск из консоли: ```./hw1.py --keys params```.

Список ключей:

* ```--help``` -- отображает всю доступную информацию по ключам,
 * ```--start $num_users $base_bir``` -- запускает в tmux ```num_users``` изолированных окружений(создает директории ```base_dir/n```) Jupyter. По умолчанию ```base\_dir = ./```,
 * ```-stop $session_name $num``` -- останавливает ```num``` по счету окружение Jupyter в ```session_name```,
 * ```--stop_all $session_name``` -- останавливает все окружения Jupyter в ```session_name```.