min=1000000
max=-1000000
n = int(input())
l = []
l.extend(map(int, input().split()))
for i in l:
    if(min > i):
        min = i
    if(max < i):
        max = i
print(min, max)