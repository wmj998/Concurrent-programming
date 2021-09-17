import threading


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(length):
    for arc in range(length):
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + str(arc))


# 创建线程
thread = threading.Thread(target=action, args=(20,))

'''
当程序中主线程及所有非守护线程执行结束时，未执行完毕的守护线程也会随之消亡（进行死亡状态），程序将结束运行。
'''

# 将thread设置为守护线程
thread.daemon = True
# thread = threading.Thread(target=action, args=(20,), daemon=True)

# 启动线程
thread.start()

# 主线程执行如下语句
for i in range(5):
    print(threading.current_thread().getName())
