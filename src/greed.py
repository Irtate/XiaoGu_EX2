import matplotlib.pyplot as plt
import time

def greed(N, V, v, w):
    # 程序运行时间
    start = time.time()

    # 贪心算法
    f = [[0]*(V+1) for _ in range(N+1)]
    r = [0] * (N+1)
    for i in range(1, N+1):
        r[i] = w[i] / v[i]

    r.sort()

    res = 0
    for i in range(1, N+1):
        if r[i] <= V:
           res = res + r[i]*v[i]

    # 程序结束运行时间计算
    end = time.time()

    print("使用贪心算法所得的最高价值为{:d},运行时间为{:f}s;".format(res, end - start))

    s = "使用贪心算法所得的最高价值为{:d},运行时间为{:f}s;".format(res, end - start) + "\n"
    file = open('data/txt/greed.txt', 'w')
    file.write(s)
    file.close()