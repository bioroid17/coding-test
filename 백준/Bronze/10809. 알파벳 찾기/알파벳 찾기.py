s=input()
for i in range(ord('a'), ord('z')+1):
    j = 0
    while j < len(s):
        if(ord(s[j]) == i):
            print(j, end=" ")
            break
        j += 1
    else:
        print("-1", end=" ")