import numpy as np


def matrix_chain_order(p):
    n = len(p) - 1
    m = np.zeros((n, n))
    s = np.zeros((n, n))

    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l -1
            m[i-1][j-1] = float('inf')

            for k in range(i, j):
                q = m[i-1][k-1] + m[k][j-1] + p[i-1] * p[k] * p[j]
                if q < m[i-1][j-1]:
                    m[i-1][j-1] = q
                    s[i-1][j-1] = k

    return m, s


def print_optimal_parens(s, i, j):
    if i == j:
        print('A', i, sep='',end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, int(s[i-1][j-1]))
        print_optimal_parens(s, int(s[i-1][j-1])+1, j)
        print(')', end='')


p = [5, 10, 3, 12, 5, 50, 6]
m, s = matrix_chain_order(p)
print(m)
print(s)
print_optimal_parens(s, 1, 6)