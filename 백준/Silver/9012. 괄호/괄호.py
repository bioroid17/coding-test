testcase = int(input())
for i in range(testcase):
    stack = []
    vps = input()
    for s in vps:
        if s == '(':
            stack.append(s)
        else:
            try:
                stack.pop()
            except:
                stack.append(s)
                break
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
