
X = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
Y = ['B', 'D', 'C', 'A', 'B', 'A']

def LCS_Length(x:list, y: list):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [["" for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #print(f"x = %d, y = %d", x[i], y[j])
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "NW"
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = "N"
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = "W"
    Print_LCS(b, x, m, n)

   
def Print_LCS(b, X, i, j):
    if i == 0 or j == 0:
        return
    if b[i][j] == "NW":
        Print_LCS(b, X, i - 1, j - 1)
        print(X[i - 1])
    elif b[i][j] == "N":
        Print_LCS(b, X, i - 1, j)
    else:
        Print_LCS(b, X, i, j - 1)


LCS_Length(X, Y)
#print(B)


