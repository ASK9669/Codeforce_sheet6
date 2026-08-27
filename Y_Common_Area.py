T = int(input())

for case in range(1, T + 1):
    N = int(input())

    left = -10**9
    bottom = -10**9
    right = 10**9
    top = 10**9

    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())

        left = max(left, x1)
        bottom = max(bottom, y1)
        right = min(right, x2)
        top = min(top, y2)

    width = right - left
    height = top - bottom

    if width <= 0 or height <= 0:
        area = 0
    else:
        area = width * height

    print(f"Case #{case}: {area}")
