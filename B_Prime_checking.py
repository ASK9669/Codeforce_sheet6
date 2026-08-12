n = int(input())

if n < 2:
    print("NO")
else:
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break

    print("YES" if prime else "NO")