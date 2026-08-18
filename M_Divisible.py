N, X = input().split()
X = int(X)

remainder = 0

for digit in N:
    remainder = (remainder * 10 + int(digit)) % X

if remainder == 0:
    print("YES")
else:
    print("NO")
