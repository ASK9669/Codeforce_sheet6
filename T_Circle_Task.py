X,Y,R,N = map(int,input().split())
for i in range(N):
    x,y = map(int,input().split())
    if (x-X)**2 + (y-Y)**2 <= R**2:
        print("YES")
    else:
        print("NO")
