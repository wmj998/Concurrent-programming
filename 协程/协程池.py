import gevent
from gevent import monkey, pool
monkey.patch_all()
import time


def action(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(1)


p = pool.Pool(5)
p.map(action, (i for i in range(10)))
