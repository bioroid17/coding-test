minnum, maxnum = map(int, input().split())
isprime = [True] * (maxnum+1)
isprime[0] = isprime[1] = False
for i in range(2, maxnum+1):
    if isprime[i] == False:
        continue
    else:
        for j in range(i * 2, maxnum+1, i):
            isprime[j] = False
for i in range(minnum, maxnum+1):
    if isprime[i] == True:
        print(i)
