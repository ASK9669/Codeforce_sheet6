x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())

xmin = min(x1,x2,x3,x4)
xmax = max(x1,x2,x3,x4)
ymin = min(y1,y2,y3,y4)
ymax = max(y1,y2,y3,y4)

N = int(input())

for i in range(N):
    x,y = map(int,input().split())

    if xmin <= x <= xmax and ymin <= y <= ymax:
        print("YES")
    else:
        print("NO")
