# A,B,X = map(int,input().split())
# total  = 0
# for i in range (A,B+1,X):
#     if i %X == 0:
#         total += i
# print(total)
A, B, X = map(int, input().split())

if A > B:
    A, B = B, A

first = ((A + X - 1) // X) * X
last = (B // X) * X

if first > last:
    print(0)
else:
    n = (last - first) // X + 1
    total = n * (first + last) // 2
    print(total)
