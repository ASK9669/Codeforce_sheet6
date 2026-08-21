# N = int(input())
# X= 1
# for i in range(1,N+1):
#     X = X* i
# y =len(str(X))
# print(f"Number of digits of {N}! is {y}")

import math

N = int(input())

digits = 0

for i in range(1, N + 1):
    digits += math.log10(i)

y = int(digits) + 1

print(f"Number of digits of {N}! is {y}")
