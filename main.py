from src.dp import dp
from src.greed import greed
from src.dfs import dfs

import matplotlib.pyplot as plt
import tkinter as tk

def test(x):
    location = 'data/test/beibao'+ str(x) + '.in'
    with open(location) as file_object:
        lines = file_object.readlines()

    v = [0] * (len(lines))
    w = [0] * (len(lines))
    V, N = list(map(int, lines[0].rstrip().split()))
    for i in range(1, len(lines)):
        V_, W_ = list(map(int, lines[i].rstrip().split()))
        v[i] = V_
        w[i] = W_

    dp(N, V, v, w)
    greed(N, V, v, w)
    dfs(N, V, v, w)

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
    x = int(input())
    test(x)
