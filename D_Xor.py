A, B, Q = map(int, input().split())

if Q % 3 == 1:
    print(A)
elif Q % 3 == 2:
    print(B)
else:
    print(A ^ B)

#A,B,Q = map(int,input().split())
# if Q == 1:
#     print(A)
# elif Q == 2:
#     print(B)
# else:
#     print(A^B)
