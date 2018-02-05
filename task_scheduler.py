# coding: utf8
__author__ = 'zh'

import queue
import random
import time
import types


class Task(object):
    def __init__(self, target, tid):
        self.tid = tid
        self.target = target
        self.sendval = None
        self.stack = []
        self.result = None
        self.state = 0

    def run(self):
        self.state = 1
        return self.target.send(self.sendval)


class Eventloop(object):
    task_id_seq = 0
    task_map = {}

    def __init__(self):
        self.ready_queue = queue.Queue()

    def create_task(self, target):
        tid = Eventloop.task_id_seq
        Eventloop.task_id_seq += 1
        task = Task(target, tid)
        self.task_map[tid] = task
        self.ready_queue.put(task)

    def exit(self, task):
        del self.task_map[task.tid]
        print('task %d exited with result' % task.tid, task.result)

    def schedule(self, task):
        self.ready_queue.put(task)

    def sleep(self, duration):
        pass

    def main_loop(self):
        while True:
            task = self.ready_queue.get()

            try:
                intermediate = task.run()
                if isinstance(intermediate, types.GeneratorType):
                    task.stack.append(task.target)
                    task.target = intermediate
                    task.sendval = None
                elif isinstance(intermediate, SystemCall):
                    intermediate.task = task
                    intermediate.loop = self
                    intermediate.handle()
                    continue
                else:
                    if task.stack:
                        task.target = task.stack.pop()
                        task.sendval = intermediate
                    else:
                        task.result = intermediate
                        self.exit(task)
                        continue

            except StopIteration as stop_iter:
                if task.stack:
                    task.target = task.stack.pop()
                    task.sendval = stop_iter.value
                else:
                    task.result = stop_iter.value
                    self.exit(task)
                    continue

            self.schedule(task)


class SystemCall(object):
    task = None     # which task fired this system call
    loop = None    # the scheduler

    def handle(self):
        pass


class GetTaskID(SystemCall):

    def handle(self):
        self.task.sendval = self.task.tid
        self.loop.schedule(self.task)


def task_foo():
    for i in range(0, 5):
        print('task_foo run')
        time.sleep(random.uniform(2, 5))
        yield random.randint(0, 10)


def task_bar():
    while True:
        print('task_bar yield')
        tid = yield GetTaskID()
        print('bar run, task id: ', tid)
        time.sleep(1)


def add(x, y):
    yield x + y


def top_func(a, b):
    total = yield add(a, b)
    total = yield add(total, 10000)
    print("add result", total)
    tid = yield GetTaskID()
    return tid


loop = Eventloop()
loop.create_task(task_foo())
loop.create_task(top_func(1, 2))
loop.main_loop()
