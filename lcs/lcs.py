
X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']

def LCS_Length(x:list, y: list) -> list:
    c = [[0] * (len(y)+1)] * (len(x)+1)
    print(c)
    for i in range(1, len(x)):
        for j in range(1, len(y)):
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
            else:
                c[i][j] = c[i][j - 1]

    return c

   

Z = LCS_Length(X, Y)
print(Z)

