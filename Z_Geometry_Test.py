R, S = map(int, input().split())

if S * S <= 2 * R * R:
    print("Circle")
elif 2 * R <= S:
    print("Square")
else:
    print("Complex")
