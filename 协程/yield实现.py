import time


def consumer():
    r = '*******'
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'


def produce(c):
    print(next(c))
    # print(c.send(None))
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # c.send(n)将n的值通过yield传给n, 然后用r接收yield返回的r
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == '__main__':
    c = consumer()
    produce(c)

