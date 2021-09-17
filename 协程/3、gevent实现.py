import gevent


def action(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)


g = [gevent.spawn(action, 3) for i in range(2)]
gevent.joinall(g)




# import gevent
# from gevent import monkey
# monkey.patch_all()
# import time
#
#
# def action(n):
#     for i in range(n):
#         print(gevent.getcurrent(), i)
#         time.sleep(1)
#
#
# g = [gevent.spawn(action, 3) for i in range(2)]
# gevent.joinall(g)
