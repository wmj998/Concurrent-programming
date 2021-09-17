import greenlet


def fun1():
    for i in range(3):
        print(greenlet.getcurrent(), i)
        g2.switch()


def fun2():
    for i in range(3):
        print(greenlet.getcurrent(), i)
        g1.switch()


g1 = greenlet.greenlet(fun1)
g2 = greenlet.greenlet(fun2)
g1.switch()
