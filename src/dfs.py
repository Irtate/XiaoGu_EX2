import time

bestV = 0 # 最大价值
currW = 0 # 当前背包重量
currV = 0 # 当前背包价值

def backtrack(v, w, c, n, x, i):
    global bestV, currV, currW
    if i>= n:
        if bestV<currV:
            bestV = currV
    else:
        if currW+w[i]<=c:
            x[i]=1
            currW += w[i]
            currV += v[i]
            backtrack(v, w, c, n, x, i+1)
            currW -= w[i]
            currV -= v[i]
        x[i]=0
        backtrack(v, w, c, n, x, i+1)

def dfs(N, V, v, w):
    # 程序开始运行时间计算
    start = time.time()

    n = int(N)
    c = int(V)
    x = [0 for i in range(n)]

    # 回溯算法
    backtrack(v, w, c, n, x, 0)

    # 程序结束运行时间计算
    end = time.time()

    print("使用回溯算法所得的最高价值为{:d},运行时间为{:f}s;".format(bestV, end - start))

    s = "使用回溯算法所得的最高价值为{:d},运行时间为{:f}s;".format(bestV, end - start) + "\n"
    file = open('data/txt/dfs.txt', 'w')
    file.write(s)
    file.close()