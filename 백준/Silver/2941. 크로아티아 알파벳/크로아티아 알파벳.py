string = input() + "  "
count = 0
i = 0
while(i < len(string.strip()) ):
    count += 1
    if ord(string[i]) == ord('c') and (ord(string[i+1]) == ord('=') or ord(string[i+1]) == ord('-')):
        i += 2
    elif ord(string[i]) == ord('d') and ord(string[i+1]) == ord('z') and ord(string[i+2]) == ord('='):
        i += 3
    elif ord(string[i]) == ord('d') and ord(string[i+1]) == ord('-'):
        i += 2
    elif ord(string[i]) == ord('l') and ord(string[i+1]) == ord('j'):
        i += 2
    elif ord(string[i]) == ord('n') and ord(string[i+1]) == ord('j'):
        i += 2
    elif ord(string[i]) == ord('s') and ord(string[i+1]) == ord('='):
        i += 2
    elif ord(string[i]) == ord('z') and ord(string[i+1]) == ord('='):
        i += 2
    else:
        i+=1
        continue
print(count)