import concurrent.futures


# 定义一个函数，用于计算一个数的平方
def square_number(n):
    return n * n


if __name__ == "__main__":
    # 创建一个包含 3 个线程的线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        # 提交任务到线程池
        results = [executor.submit(square_number, i) for i in range(5)]

        # 获取任务的结果
        for future in concurrent.futures.as_completed(results):
            print(future.result())
