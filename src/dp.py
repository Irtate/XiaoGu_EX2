import time

def dp(N, V, v, w):
    # 程序开始运行时间计算
    start = time.time()

    # 动态规划
    f = [0] * (V + 1)
    for i in range(1, N+1):
        for j in range(V, v[i]-1,-1):
            f[j] = max(f[j], f[j-v[i]]+w[i])

    # 程序结束运行时间计算
    end = time.time()

    print("使用动态规划算法所得的最高价值为{:d},运行时间为{:f}s;".format(f[V], (end - start)))

