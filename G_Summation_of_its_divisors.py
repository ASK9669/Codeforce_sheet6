# N = int(input())
# total = 0
# for i in range(1,N+1):
#     if N%i == 0:
#         total += i
# print(total)

N = int(input())
total = 0

i = 1
while i * i <= N:
    if N % i == 0:
        total += i

        if i != N // i:
            total += N // i

    i += 1

print(total)
