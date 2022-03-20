import time

def greed(N, V, v, w):
    # 程序运行时间
    start = time.time()

    # 贪心算法
    r = [0] * (N+1)
    for i in range(1, N+1):
        r[i] = w[i] / v[i]

    for i in range(1, N):
        for j in range(i+1, N+1):
            if r[i] < r[j]:
                tmp_v = v[i]
                tmp_w = w[i]
                tmp_r = r[i]
                v[i] = v[j]
                w[i] = w[j]
                r[i] = r[j]
                v[j] = tmp_v
                w[j] = tmp_w
                r[j] = tmp_r

    res = 0
    for i in range(N, 0, -1):
        if v[i] <= V:
            res = res + int(r[i]*v[i])
            V -= v[i]

    # 程序结束运行时间计算
    end = time.time()

    print("使用贪心算法所得的最高价值为{:d},运行时间为{:f}s;".format(res, end - start))

    s = "使用贪心算法所得的最高价值为{:d},运行时间为{:f}s;".format(res, end - start) + "\n"
    file = open('data/txt/greed.txt', 'w')
    file.write(s)
    file.close()