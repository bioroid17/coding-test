from math import sqrt
t = int(input())
while t > 0:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = sqrt((x1- x2)**2 + (y1 - y2)**2)
    if r1 == r2 and d == 0:
        print("-1")
    elif abs(r1-r2) < d and d < abs(r1+r2):
        print("2")
    elif abs(r1-r2) == d or abs(r1+r2) == d:
        print("1")
    elif abs(r1-r2) > d or abs(r1+r2) < d:
        print("0")
    t -= 1