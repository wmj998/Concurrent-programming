# 调用Thread类的构造器创建线程
import threading


# 定义线程要调用的方法，*add可接收多个以非关键字方式传入的参数
def action(*add):
    for arc in add:
        # 调用 getName() 方法获取当前执行该程序的线程名
        print(threading.current_thread().getName() + " " + arc)


# 定义为线程方法传入的参数
my_tuple = ("http://c.biancheng.net/python/", \
            "http://c.biancheng.net/shell/", \
            "http://c.biancheng.net/java/")

# 创建线程
thread = threading.Thread(target=action, args=my_tuple)
thread.start()

for i in range(5):
    print(threading.current_thread().getName())




# # 继承Thread类创建线程类
# import threading
#
#
# # 创建子线程类，继承自 Thread 类
# class my_Thread(threading.Thread):
#     def __init__(self, add):
#         threading.Thread.__init__(self)
#         self.add = add
#
#     # 重写run()方法
#     def run(self):
#         for arc in self.add:
#             # 调用 getName() 方法获取当前执行该程序的线程名
#             print(threading.current_thread().getName() + " " + arc)
#
#
# # 定义为 run() 方法传入的参数
# my_tuple = ("http://c.biancheng.net/python/", \
#             "http://c.biancheng.net/shell/", \
#             "http://c.biancheng.net/java/")
#
# # 创建子线程
# mythread = my_Thread(my_tuple)
#
# # 启动子线程
# mythread.start()
#
# # 主线程执行此循环
# for i in range(5):
#     print(threading.current_thread().getName())
