#!/usr/bin/env python3

from argparse import ArgumentParser
# from todo_api import TodoAPI
# from todo_erppeek import TodoAPI
from todo_odoorpc import TodoAPI

parser = ArgumentParser()
parser.add_argument(
    'command',
    choices=['list', 'add', 'del', 'done'])
parser.add_argument('text', nargs='?')
args = parser.parse_args()

srv, port, db = 'localhost', 8069, 'todo'
user, pwd = 'admin', 'admin'
api = TodoAPI(srv, port, db, user, pwd)

if args.command == 'list':
    todos = api.read()
    for todo in todos:
        todo['done'] = 'X' if todo['is_done'] else ' '
        print('%(id)d [%(done)s] %(name)s' % todo)

if args.command == 'add':
    todo_id = api.write(args.text)
    print('Todo %d created.' % todo_id)

if args.command == 'del':
    todo_id = api.unlink(int(args.text))
    print('Todo %s was deleted.' % args.text)
