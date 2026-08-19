T = int(input())
N, X = input().split()
X = int(X)

if T == 1:
    # Base X -> Decimal
    ans = 0

    for digit in N:
        if digit.isdigit():
            value = int(digit)
        else:
            value = ord(digit) - ord('A') + 10

        ans = ans * X + value

    print(ans)

else:
    # Decimal -> Base X
    N = int(N)

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans = ""

    while N > 0:
        remainder = N % X
        ans += digits[remainder]
        N //= X

    print(ans[::-1])
