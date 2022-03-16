import matplotlib.pyplot as plt
import time

def greed(N, V, v, w):
    # 程序运行时间
    start = time.time()

    # 贪心算法
    f = [[0]*(V+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(0, V+1):
            f[i][j] = f[i-1][j]
            if j >= v[i]:
                f[i][j] = max(f[i][j], f[i-1][j-v[i]]+w[i])

    # 程序结束运行时间计算
    end = time.time()

    print("使用贪心算法所得的最高价值为{:d},运行时间为{:f}s;".format(f[N][V], end - start))