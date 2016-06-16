__author__ = 'zh'

import Queue
import time
import random


class Task(object):
    def __init__(self, target, tid):
        self.target = target
        self.sendval = None
        self.tid = tid

    def Run(self):
        return self.target.send(self.sendval)


class Scheduler(object):
    task_id = 0
    task_map = {}

    def __init__(self):
        self.ready_queue = Queue.Queue()

    def NewTask(self, target):
        tid = Scheduler.task_id
        Scheduler.task_id += 1
        task = Task(target, tid)
        self.task_map[tid] = task
        self.ready_queue.put(task)

    def Exit(self, task):
        print 'task %d exited' % task.tid
        del self.task_map[task.tid]

    def Schedule(self, task):
        self.ready_queue.put(task)

    def MainLoop(self):
        while True:
            task = self.ready_queue.get()
            if task:
                try:
                    result = task.Run()
                    if isinstance(result, SystemCall):
                        result.task = task
                        result.sched = self
                        result.Handle()
                        continue
                except StopIteration:
                    self.Exit(task)
                    continue

                self.Schedule(task)


class SystemCall(object):
    task = None     # which task fires this system call
    sched = None    # the scheduler
    def Handle(self):
        pass


class GetTaskID(SystemCall):
    def Handle(self):
        self.task.sendval = self.task.tid
        self.sched.Schedule(self.task)


def task_foo():
    for i in range(0, 5):
        print 'foo run'
        time.sleep(random.uniform(0, 2))
        yield random.randint(0, 10)


def task_bar():
    while True:
        tid = yield GetTaskID()
        print 'bar run, task id: ', tid
        time.sleep(1)


sched = Scheduler()
sched.NewTask(task_foo())
sched.NewTask(task_bar())

sched.MainLoop()
