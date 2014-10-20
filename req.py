import time
import gevent
from gevent import queue
from gevent import monkey
import requests

gevent.monkey.patch_all(socket=True, dns=True, time=True, select=True, thread=True, os=True, 
    ssl=True, httplib=False, subprocess=False, sys=False, aggressive=True, Event=False)

import threading
# gevent.monkey.patch_socket(dns=True, aggressive=True)
# gevent.monkey.patch_time()
# gevent.monkey.patch_httplib()

start = time.time()
tic = lambda: '%1.5f seconds' % (time.time() - start)

URL = 'http://confirmtktapinew.azurewebsites.net/api/pnr/status/'
PNR = 4401134780

def do_work(item):
    tries = 0
    r = requests.get(URL + str(item))
    while r.status_code != 200:
        if tries > 10:
            break;
        r = requests.get(URL + str(item))
        tries += 1
    if r.status_code == 200:
        x = r.json()
        print item - PNR, x
        #x is dict you need to perform stuff upon
    else:
        print "%s error" % item - PNR

def worker():
    while True:
        item = task_queue.get()
        try:
            do_work(item)
        finally:
            task_queue.task_done()


task_queue = gevent.queue.JoinableQueue()

num_worker_threads = 10
num_tasks = 100

start = time.time()

for i in xrange(num_worker_threads):
    x = gevent.spawn(worker)

print 'Time taken to spawn %s workers' % num_worker_threads, tic()

for item in xrange(num_tasks):
    task_queue.put(PNR + item)

start = time.time()

task_queue.join()  # block until all tasks are done

print 'Time taken for %s tasks ' % num_tasks, tic()