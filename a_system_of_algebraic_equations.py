from fractions import Fraction


def get_row(num):
    num -= 1
    global n, a
    ans = []
    for i in range(n):
        ans.append(Fraction(a[i][num]))
        # ans.append(round(a[i][num], 8))
    return ans


def scal_mult(vect1, vect2):
    global n
    ans = 0
    for i in range(n):
        ans += vect1[i] * vect2[i]
    return Fraction(ans)
    # return round(ans, 8)


def vect_mult(vect, x):
    global n
    ans = []
    for i in range(n):
        ans.append(Fraction(vect[i] * x))
        # ans.append(round(vect[i] * x, 8))
    return ans


def rows_subtraction(row1, row2):
    global n
    ans = []
    for i in range(n):
        ans.append(Fraction(row1[i] - row2[i]))
        # ans.append(round(row1[i] - row2[i], 8))
    return ans


def ortogonalizaciya():
    global n, a, b
    a1 = get_row(1)
    r1 = a1

    a2 = get_row(2)
    r2 = rows_subtraction(a2, vect_mult(r1, scal_mult(a2, r1) / scal_mult(r1, r1)))
    a3 = get_row(3)
    r3 = rows_subtraction(rows_subtraction(a3, vect_mult(r1, scal_mult(a3, r1) / scal_mult(r1, r1))),
                          vect_mult(r2, scal_mult(a3, r2) / scal_mult(r2, r2)))
    x3 = scal_mult(b, r3) / scal_mult(a3, r3)
    b1 = rows_subtraction(b, vect_mult(a3, x3))
    x2 = scal_mult(b1, r2) / scal_mult(a2, r2)
    print(b1, r2, a2, r2)
    print(scal_mult(b1, r2), scal_mult(a2, r2))
    b2 = rows_subtraction(b1, vect_mult(a2, x2))
    x1 = scal_mult(b2, r1) / scal_mult(a1, r1)
    print("a1", for_print(a1), end='; ');print("a2", for_print(a2), end='; ');print("a3", for_print(a3));
    print("r1", for_print(r1), end='; ');print("r2", for_print(r2), end='; ');print("r3", for_print(r3));
    print("b0", for_print(b), end='; ');print("b1", for_print(b1), end='; ');print("b2", for_print(b2));
    # x1 = float(x1); x2 = float(x2); x3 = float(x3)
    print("x1", x1, end='; ');print("x2", x2, end='; ');print("x3", x3);


def jordan_gaus():
    global n, a, b
    for i in range(n):
        print_slau()
        x = a[i][i]
        for j in range(i, n):
            a[i][j] = Fraction(a[i][j], x)
            # a[i][j] /= x
        b[i] = Fraction(b[i], x)
        print_slau()
        # b[i] /= x
        for j in range(i + 1, n):
            x = a[j][i]
            for k in range(n):
                a[j][k] = Fraction(a[j][k] - a[i][k] * x)
                # a[j][k] -= a[i][k] * x
            b[j] = Fraction(b[j] - b[i] * x)
            # b[j] -= b[i] * x
    # print_slau()
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            b[j] = Fraction(b[j] - a[j][i] * b[i])
            # b[j] -= a[j][i] * b[i]
            a[j][i] = 0
        print_slau()
    # print_slau()
    print(*b)


def gaus():
    global n, a, b
    for i in range(n):
        print_slau()
        x = a[i][i]
        for j in range(i, n):
            # a[i][j] /= x
            a[i][j] = Fraction(a[i][j], x)
        # b[i] /= x
        b[i] = Fraction(b[i], x)
        print_slau()
        for j in range(i + 1, n):
            x = a[j][i]
            for k in range(n):
                # a[j][k] -= a[i][k] * x
                a[j][k] = Fraction(a[j][k] - a[i][k] * x)
            # b[j] -= b[i] * x
            b[j] = Fraction(b[j] - b[i] * x)
    # print_slau()
    ans = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        x = b[i]
        print("x", i + 1, ' = ', x, sep='', end='');
        for j in range(i + 1, n):
            # x -= a[i][j] * ans[j]
            print(" -", a[i][j], '*', ans[j], end='')
            x = Fraction(x - a[i][j] * ans[j])
        print(' =', x)
        ans[i] = x
    print(*ans)


def print_slau():
    global n, a, b
    for i in range(n):
        for j in range(n):
            # x = str(round(a[i][j], 3))
            x = str(Fraction(a[i][j]))
            print(' ' * (5 - len(x)) + x, end=' ')
        # x = str(round(b[i], 3))
        x = str(Fraction(b[i]))
        print(' ' * (5 - len(x)) + x)
    print()


def for_print(vect):
    ans = '('
    for i in vect:
        # ans += str(Fraction(i)) + ' '
        ans += str(i) + ' '
    ans = ans[:-1] + ')'
    return ans


file = open("slau.txt", 'r')
n = int(file.readline())
a = [[] for i in range(n)]
b = []
for i in range(n):
    arr = list(map(float, file.readline().split()))
    a[i] = arr[0:n]
    b.append(arr[n])
# gaus()
# jordan_gaus()
ortogonalizaciya()
