L, R, M = map(int, input().split())

result = 1

for i in range(L, R + 1):
    result = (result * i) % M

print(result)
