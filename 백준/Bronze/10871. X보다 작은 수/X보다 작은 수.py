n, x = map(int, input().split())
l = []
l.extend(map(int, input().split()))
for i in l:
    if(i < x):
        print(i, end=" ")