sec = 0
string = input()
phone = ["", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
for i in string:
    for j in phone:
        if(j.find(i)==-1):
            continue
        else:
            sec += (phone.index(j) + 1)
            break
print(sec)