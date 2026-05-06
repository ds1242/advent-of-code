
X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']

def LCS_Length(x:list, y: list):
    c = [[0]*(len(y)+1) for _ in range(len(x) + 1)]
    b = [[""]*(len(y)+1) for _ in range(len(x) + 1)]
    print(c)
    for i in range(0, len(x)):
        for j in range(0, len(y)):
            #print(f"x = %d, y = %d", x[i], y[j])
            if x[i] == y[j]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "NW"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "N"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "W"

    return c, b

   

Z, B = LCS_Length(X, Y)
print(Z)
# print(B)

