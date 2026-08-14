ra, ca = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(ra)]

rb, cb = map(int, input().split())

B = [list(map(int, input().split())) for _ in range(rb)]

C = [[0] * cb for _ in range(ra)]

for i in range(ra):
    for j in range(cb):
        for k in range(ca):
            C[i][j] += A[i][k] * B[k][j]

for row in C:
    print(*row)
