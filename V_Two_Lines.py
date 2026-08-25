x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

dx1 = x2 - x1
dy1 = y2 - y1

dx2 = x4 - x3
dy2 = y4 - y3

if dx1 * dy2 == dy1 * dx2:
    print("YES")
else:
    print("NO")
