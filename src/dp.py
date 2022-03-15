import matplotlib.pyplot as plt

def dp(N, V, v, w):
    f = [0] * (V + 1)

    for i in range(1, N+1):
        for j in range(V, v[i]-1,-1):
            f[j] = max(f[j], f[j-v[i]]+w[i])

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.scatter(v, w, s=10)
    plt.show()

    print(f[V])