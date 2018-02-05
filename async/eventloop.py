# coding=utf8

import asyncio
import aiohttp
import async_timeout


async def func():
    total = 0
    for i in range(0, 10):
        total += i
        print(total)
        await asyncio.sleep(0.1)
    return total


def foo_param():
    print("foo param")
    return 1234


def bar_param():
    print("bar param")
    return 4321


async def foo(n, m=bar_param()):
    r = await func()
    print(r)


result_of_calling_foo = foo(foo_param())  # Function foo is not called, but the arguments are evaluated.
print("result_of_calling_foo: ", result_of_calling_foo)
print(result_of_calling_foo.cr_frame.f_locals)


@asyncio.coroutine
def fetch_page(url):
    with aiohttp.ClientSession() as session:
        try:
            response = yield from asyncio.wait_for(session.request('GET', url), timeout=2)
            print('URL: {0}:  Status: {1}'.format(url, response.status))
        except asyncio.TimeoutError:
            print('URL: {0} timeout'.format(url))


@asyncio.coroutine
def fetch_page_with_timeout(url, timeout):
    try:
        with async_timeout.timeout(timeout):
            response = yield from aiohttp.request('GET', url)
            print('URL: {0}:  Status: {1}'.format(url, response.status))
    except asyncio.TimeoutError:
        print('URL: {0} timeout'.format(url))


tasks = [
    result_of_calling_foo,
    fetch_page('http://baidu.com'),
    fetch_page('http://alibaba.com'),
    fetch_page('http://tencent.com'),
    fetch_page_with_timeout("http://google.com", 3)
]

loop = asyncio.get_event_loop()
loop.create_task(result_of_calling_foo)
loop.run_until_complete(asyncio.wait(tasks))

loop.shutdown_asyncgens()
loop.close()
