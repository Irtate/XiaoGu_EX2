from src.dp import dp

if __name__ == '__main__':
    with open('data/test/beibao0.in') as file_object:
        lines = file_object.readlines()

    v = [0] * (len(lines))
    w = [0] * (len(lines))
    V, N = list(map(int, lines[0].rstrip().split()))
    for i in range(1, len(lines)):
        V_, W_ = list(map(int, lines[i].rstrip().split()))
        v[i] = V_
        w[i] = W_

    dp(N, V, v, w)