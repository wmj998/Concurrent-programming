from threading import Timer


def hello():
    print("hello, world")


# 指定10秒后执行hello函数
t = Timer(10.0, hello)
t.start()




# from threading import Timer
# import time
#
# # 定义总共输出几次的计数器
# count = 0
#
#
# def print_time():
#     print("当前时间：%s" % time.ctime())
#     global t, count
#     count += 1
#     # 如果count小于10，开始下一次调度
#     if count < 10:
#         t = Timer(1, print_time)
#         t.start()
#
#
# # 指定1秒后执行print_time函数
# t = Timer(1, print_time)
# t.start()
