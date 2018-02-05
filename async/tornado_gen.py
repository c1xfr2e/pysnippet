# coding: utf8
__author__ = 'zh'

import heapq

from tornado import gen
from tornado.platform import select


@gen.coroutine
def some_function(*args, **kwargs):
    print('in some_function', args)

    sleep_future = gen.sleep(3)
    yield sleep_future
    print('wakeup from sleep')

    raise gen.Return("Some Function Returned Some Shit")


@gen.coroutine
def call_task(x):
    future_from_func_a = some_function()
    future_from_func_a.name = "some_function_a"
    yield future_from_func_a

    future_from_func_b = some_function()
    b_result = yield future_from_func_b
    print(b_result)

    another_future = gen.Task(some_function, 'hello')
    result = yield another_future
    print('result of gen.Task', result)

    raise gen.Return(x + 1000)


@gen.coroutine
def main():
    print('main() sleep')

    call_task_future = yield call_task(3)
    f = yield call_task_future
    print(f)

    print('main() wakeup')


if __name__ == '__main__':
    loop = select.SelectIOLoop()
    loop.add_callback(main)
    loop.start()
    print('exit')
