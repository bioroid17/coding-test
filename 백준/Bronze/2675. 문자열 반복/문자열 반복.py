t = int(input())
while(t > 0):
    r, s = input().split()
    r = int(r)
    for i in s:
        for j in range(r):
            print(i, end="")
    print()
    t -= 1