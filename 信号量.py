import threading
import time
from concurrent.futures import ThreadPoolExecutor


def action(semaphore):
    semaphore.acquire()
    print(threading.current_thread().name, threading.current_thread().ident)
    time.sleep(1)
    semaphore.release()


semaphore = threading.Semaphore(2)
with ThreadPoolExecutor(max_workers=4) as pool:
    results = pool.map(action, tuple(semaphore for i in range(10)))
