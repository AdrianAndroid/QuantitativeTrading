import threading

# 共享资源
counter = 0
# 创建锁对象
lock = threading.Lock()


# 定义线程要执行的函数，用于增加计数器的值
def increment():
    global counter
    for _ in range(100000):
        # 获取锁
        lock.acquire()
        try:
            counter += 1
        finally:
            # 释放锁
            lock.release()


if __name__ == "__main__":
    # 创建两个线程
    thread1 = threading.Thread(target=increment)
    thread2 = threading.Thread(target=increment)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程执行完毕
    thread1.join()
    thread2.join()

    print(f"最终计数器的值: {counter}")
