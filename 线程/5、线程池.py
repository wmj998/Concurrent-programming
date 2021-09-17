from concurrent.futures import ThreadPoolExecutor  # 线程池
from concurrent.futures import ProcessPoolExecutor  # 进程池
import threading
import time


# 定义一个准备作为线程任务的函数
def action(max):
    my_sum = 0
    for i in range(max):
        print(threading.current_thread().name + '  ' + str(i))
        my_sum += i
    return my_sum


# 创建一个包含2条线程的线程池
pool = ThreadPoolExecutor(max_workers=2)

# 向线程池提交一个task, 50会作为action()函数的参数
future1 = pool.submit(action, 50)

# 向线程池再提交一个task, 100会作为action()函数的参数
future2 = pool.submit(action, 100)

# 判断future1代表的任务是否结束
print('future1', future1.done())
time.sleep(3)

# 判断future2代表的任务是否结束
print('future2', future2.done())

# 查看future1代表的任务返回的结果
print(future1.result())

# 查看future2代表的任务返回的结果
print(future2.result())

# 关闭线程池
pool.shutdown()

print('--------------')




# from concurrent.futures import ThreadPoolExecutor
# import threading
#
#
# # 定义一个准备作为线程任务的函数
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         print(threading.current_thread().name + '  ' + str(i))
#         my_sum += i
#     return my_sum
#
#
# '''
# 由于线程池实现了上下文管理协议（Context Manage Protocol），
# 因此，程序可以使用 with 语句来管理线程池，这样即可避免手动关闭线程池。
# '''
# # 创建一个包含2条线程的线程池
# with ThreadPoolExecutor(max_workers=2) as pool:
#     # 向线程池提交一个task, 50会作为action()函数的参数
#     future1 = pool.submit(action, 50)
#     # 向线程池再提交一个task, 100会作为action()函数的参数
#     future2 = pool.submit(action, 100)
#
#
#     def get_result(future):
#         print(future.result())
#
#
#     # 为future1添加线程完成的回调函数
#     future1.add_done_callback(get_result)
#
#     # 为future2添加线程完成的回调函数
#     future2.add_done_callback(get_result)
#
# print('--------------')




# from concurrent.futures import ThreadPoolExecutor
# import threading
#
#
# # 定义一个准备作为线程任务的函数
# def action(max):
#     my_sum = 0
#     for i in range(max):
#         print(threading.current_thread().name + '  ' + str(i))
#         my_sum += i
#     return my_sum
#
#
# # 创建一个包含4条线程的线程池
# with ThreadPoolExecutor(max_workers=4) as pool:
#     # 使用线程执行map计算，map()方法的返回值将会收集每个线程任务的返回结果
#     # 后面元组有3个元素，因此程序启动3条线程来执行action函数
#     results = pool.map(action, (50, 100, 150))
#     print('--------------')
#     for r in results:
#         print(r)
