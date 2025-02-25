import threading


# 定义第一个线程要执行的函数
def print_numbers():
    for i in range(5):
        print(f"线程 1 打印数字: {i}")


# 定义第二个线程要执行的函数
def print_letters():
    for letter in 'abcde':
        print(f"线程 2 打印字母: {letter}")


if __name__ == "__main__":
    # 创建线程对象
    thread1 = threading.Thread(target=print_numbers)
    thread2 = threading.Thread(target=print_letters)

    # 启动线程
    thread1.start()
    thread2.start()

    # 等待线程执行完毕
    thread1.join()
    thread2.join()

    print("所有线程执行完毕。")
