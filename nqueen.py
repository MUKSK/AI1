def print_board(x, n):
    for i in range(1, n + 1):
        row = ['.'] * n
        row[x[i] - 1] = 'Q'
        print(" ".join(row))
    print()

def place(x, k, i):
    for j in range(1, k):
        if x[j] == i or abs(j - k) == abs(x[j] - i):
            return False
    return True

def Nqueens(n, k, x):
    for i in range(1, n + 1):
        if place(x, k, i):
            x[k] = i
            if k == n:
                print_board(x, n)
            else:
                Nqueens(n, k + 1, x)

n = 4
x = [0] * (n + 1)
Nqueens(n, 1, x)