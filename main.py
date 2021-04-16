"""
DESCRIPTION:    This program provides resolving linear equation systems like Ax=B with gauss' method.

INPUT:          firstly you should input the coefficient matrix A size: 'n m' ENTER
                secondly you should input the first row coefficients A B divided by ' ' ENTER
                then you should input all remaining rows the same way.
                (example:   3 3
                            1 2 3 4
                            5 4 3 2
                            1 9 7 3
                )

OUTPUT:         the matrix after straight algorithm move
                the matrix after reverse algorithm move
                does the equation system have single solution or INF if it has infinite amount of solutions
                (if the system has solutions: the solution vector x)
"""


def round_row(row):
    for i in range(len(row)):
        row[i] = round(row[i], 3)


def sub_rows(dec, sub, div):
    for i in range(len(dec)):
        dec[i] = dec[i] - sub[i] * div


def check_row(row):
    s = 0
    for i in range(len(row) - 1):
        s += row[i] ** 2

    if s:
        return 1
    elif row[-1]:
        return 0
    else:
        return -1


def get_resolves(mx, n, m):
    result = ['YES']
    for i in range(n):
        if check_row(mx[i]) == 1:
            result.append(mx[i][-1])
        elif check_row(mx[i]) == -1:
            result = ['INF']
            break
        else:
            result = ['NO']
            break

    if n < m and result[0] != 'NO':
        result = ['INF']

    return result


def straight_move(mx, n, m, restart=0):
    for i in range(restart, min(n, m)):
        round_row(mx[i])
        div1 = mx[i][i]

        if div1:
            mx[i] = list(map(lambda c: round(c / div1, 3), mx[i]))

            for j in range(i + 1, n):
                div2 = mx[j][i]
                sub_rows(mx[j], mx[i], div2)
        else:
            row = mx.pop(i)
            mx.append(row)
            print('Matrix after straight move -{}- (rec): {}'.format(i, mx))

            div = list(filter(lambda c: c == 0.0, row[:min(n, m)]))[0]
            if div:
                straight_move(mx, n, m, restart=i+1)
            else:
                straight_move(mx, n - 1, m, restart=i)
            break

    print('Matrix after straight move: {}'.format(mx))


def reverse_move(mx, n, m):
    for i in range(min(n, m) - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            div = mx[j][i]
            sub_rows(mx[j], mx[i], div)

    print('Matrix after reverse move: {}'.format(mx))


def print_results(result):
    print(result.pop(0))
    print(' '.join([str(x) for x in result]))


n, m = map(int, input().split())
matrix = []
for i in range(n):
    row = list(map(float, input().split()))
    matrix.append(row)

straight_move(matrix, n, m)
reverse_move(matrix, n, m)
res = get_resolves(matrix, n, m)
print_results(res)