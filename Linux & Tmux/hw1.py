#!/usr/bin/python3

import libtmux
import os
import tqdm
import argparse


def start(num_users, base_dir='./'):
    """
    Запустить $num_users ноутбуков. У каждого рабочай директория $base_dir+$folder_num
    """
    server = libtmux.Server()
    session = server.new_session('jupyter notebooks')
    ip = '127.0.0.1'
    for i in tqdm.tqdm(range(num_users)):
        current_dir = base_dir + "{}".format(i)
        curr_port = 10786 + i
        if not os.path.isdir(current_dir):
            os.mkdir(current_dir)
        if session.get_by_id('@{}'.format(i)):
            window = session.get_by_id('@{}'.format(i))
        else:
            window = session.new_window(current_dir)
        pane = window.attached_pane
        pane.send_keys(
            'jupyter notebook --ip {} --port {} --no-browser --NotebookApp.notebook_dir="{}"'
            .format(ip, curr_port, current_dir))


def stop(session_name, num):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    @:param num: номер окружения, кот. можно убить
    """
    server = libtmux.Server()
    session = server.find_where({'session_name': session_name})
    if not session:
        raise ValueError('Incorrect session name')
    window = session.get_by_id('@{}'.format(num))
    if not window:
        raise ValueError('Incorrect number')
    try:
        window.kill_window()
    except libtmux.exc.LibTmuxException:
        pass


def stop_all(session_name):
    """
    @:param session_name: Названия tmux-сессии, в которой запущены окружения
    """
    server = libtmux.Server()
    session = server.find_where({'session_name': session_name})
    if not session:
        raise ValueError('Incorrect session name')
    try:
        session.kill_session()
    except libtmux.exc.LibTmuxException:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', nargs='+',
                        help="starts $num_users jupyter notebooks in working directory $base_dir + $folder_num")
    parser.add_argument('--stop', nargs='+',
                        help="stop $num window in $session_name")
    parser.add_argument('--stop_all', nargs='+',
                        help="stops all launched jupyter notebooks in $session_name")
    args = parser.parse_args()
    try:
        if args.start:
            num_users = int(args.start[0])
            base_dir = './'
            if len(args.start) > 1:
                base_dir = args.start[1]
            start(num_users=num_users, base_dir=base_dir)
        if args.stop:
            session_name = args.stop[0]
            num = args.stop[1]
            stop(session_name=session_name, num=num)
        if args.stop_all:
            session_name = args.stop_all[0]
            stop_all(session_name=session_name)
    except IndexError:
        print('You didn\'t provide enough values')


if __name__ == "__main__":
    main()
