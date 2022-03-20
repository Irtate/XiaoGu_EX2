from src.dp import dp
from src.greed import greed
from src.dfs import dfs

import matplotlib.pyplot as plt
import tkinter as tk

def test(x):
    file = open('data/txt/a.txt', 'w')

    location = 'data/test/beibao'+ str(x) + '.in'
    with open(location) as file_object:
        lines = file_object.readlines()

    v = [0] * (len(lines))
    w = [0] * (len(lines))
    r = [0.0] * (len(lines))

    V, N = list(map(int, lines[0].rstrip().split()))
    for i in range(1, len(lines)):
        V_, W_ = list(map(int, lines[i].rstrip().split()))
        v[i] = V_
        w[i] = W_

    print("请选择使用的算法[0:动态规划, 1:贪心算法; 2:回溯算法]:")
    op = int(input())

    if op == 0:
        dp(N, V, v, w)
    elif op == 1:
        greed(N, V, v, w)
    else:
        dfs(N, V, v, w)

    for i in range(1, len(lines)):
        r[i] = w[i] / v[i]

    print("按照价值比非递增排序输出:")
    file.write("按照价值比非递增排序输出:")
    r.sort()
    j = 1
    for i in range(len(lines)-1, 1, -1):
        s = "第{:d}个物品的价值比为:{:.6f};".format(j,r[i])
        file.write(s + "\n")
        print(s)
        j = j + 1

    file.close()

    # 绘制散点图
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(v, w, s=10)
    plt.xlabel('体积', fontproperties='KaiTi')
    plt.ylabel('价值', fontproperties='KaiTi')
    plt.title('体积与价值变量散点图', fontproperties='KaiTi')
    plt.show()



if __name__ == '__main__':
    # 图形界面设计
    # root = tk.Tk()
    # root.geometry("600x400+500+200")
    #
    # # 标签设计
    # lab1 = tk.Label(root, text="个人软件项目", font=("华文行楷",20))
    # lab1.pack()
    #
    # # 输入设计
    # L1 = tk.Label(root, text="网站名")
    # L1.pack()
    # E1 = tk.Entry(root, bd=5)
    # E1.pack()
    #
    # # 按钮设计
    # btn1 = tk.Button(root, text="确定", compound=callback())
    # btn1.pack()
    #
    # root.mainloop()
    print("请输入需要测试的数据[0~9]:")
    x = int(input())
    test(x)
