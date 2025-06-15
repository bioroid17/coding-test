t = int(input())
while t > 0:
    l = []
    sum = 0
    count = 0
    l.extend(map(int, input().split()))
    student = l[0]
    for i in range(1, len(l)):
        sum += l[i]
    avg = sum / l[0]
    for i in range(1, len(l)):
        if l[i] > avg:
            count += 1
    print("%.3f" % (count/l[0]*100) + "%")
    t -= 1