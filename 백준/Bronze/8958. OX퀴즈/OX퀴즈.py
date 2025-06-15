l=[]
n = int(input())
for i in range(n):
    score = 0
    combo = 0
    l.append(input())
    for j in l[i]:
        if ord(j) == ord('O'):
            combo += 1
            score += combo
        else:
            combo = 0
    print(score)