n = int(input())
cycle = 0
a = b = 0
result = n
while(True):
    cycle += 1
    a = result // 10
    b = result % 10
    result = b * 10 + (a + b) % 10
    if(result == n):
        break
print(cycle)
