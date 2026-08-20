# N = int(input())
# print(N+9999)
# print(N*9999)

import sys

sys.set_int_max_str_digits(20000)

N = int(input())

print(N + 9999)
print(N * 9999)
