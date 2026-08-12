# A,B = map(int,input().split())
# def Sum(x,y):
#    total = (x + y) * (y - x + 1) // 2
#    return total

# def sum_even(x,y):
#     total = 0
#     for i in range(x, y + 1):
#         if i % 2 == 0:
#             total += i
#     return total
# def sum_odd(x,y):
#     total = 0
#     for i in range(x, y + 1):
#         if i % 2 != 0:
#             total += i
#     return total

# if B < A:
#     A,B = B,A

# print(Sum(A,B))
# print(sum_even(A,B))
# print(sum_odd(A,B))

A, B = map(int, input().split())
if A > B:
    A, B = B, A
total = (A + B) * (B - A + 1) // 2
first_even = A if A % 2 == 0 else A + 1
last_even = B if B % 2 == 0 else B - 1
n_even = (last_even - first_even) // 2 + 1 if first_even <= last_even else 0
even_sum = n_even * (first_even + last_even) // 2
odd_sum = total - even_sum

print(total)
print(even_sum)
print(odd_sum)
