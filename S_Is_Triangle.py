# import math
A,B,C = map(int,input().split())
s = (A+B+C)//2
Area = (s * (s-A) * (s-B) * (s-C)) ** 0.5
if (((A+B) > C) and ((A+C) > B) and ((C+B) > A)):
    print("Valid")
    print(f"{Area:.6f}")
else:
    print("Invalid")
