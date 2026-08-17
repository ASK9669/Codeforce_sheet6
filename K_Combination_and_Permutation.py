A,B = map(int,input().split())
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i 
    return result
a = factorial(A)
b = factorial(B)
ab = factorial(A-B)

ncr = a//(b*ab)
npr = a//ab

print(ncr,npr)
