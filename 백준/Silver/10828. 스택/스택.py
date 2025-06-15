from sys import stdin, stdout
num = stdin.readline()
stack = []
for _ in range(int(num.rstrip())):
    cmd = stdin.readline().rstrip()
    tokens = cmd.split(" ")
    if tokens[0] == "push":
        stack.append(tokens[1])
    elif tokens[0] == "pop":
        if stack:
            stdout.write(stack.pop()+"\n")
        else:
            stdout.write("-1\n")
    elif tokens[0] == "size":
        stdout.write(str(len(stack))+"\n")
    elif tokens[0] == "empty":
        if stack:
            stdout.write("0\n")
        else:
            stdout.write("1\n")
    else:
        if stack:
            stdout.write(stack[-1]+"\n")
        else:
            stdout.write("-1\n")
