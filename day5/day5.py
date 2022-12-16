import re
file = open("input5.txt", "r").read()
data = file.splitlines()
val = (data[10:])



stack = [["G","T", "R", "W"],
 ["G", "C", "H", "P", "M", "S", "V", "W"],
 ["C", "L", "T", "S", "G", "M"],
 ["J", "H", "D", "M", "W", "R", "F"],
 ["P", "Q", "L", "H", "S", "W", "F", "J"],
 ["P", "J", "D", "N", "F", "M","S"],
 ["Z", "B", "D", "F", "G", "C", "S", "J"], 
 ["R", "T", "B"],
 ["H", "N", "W", "L", "C"]]

for i in val:
    x = re.findall('[0-9]+', i)
    num = int(x[0])
    fromBox = int(x[1])
    toBox = int(x[2])
    # print(num, fromBox, toBox)

    # new = stack[fromBox-1]
    # arr = stack[toBox-1]
    # arr = new.pop()
    arr = stack[fromBox-1][:len(stack[fromBox-1])-num]
    arr2 = stack[fromBox-1][len(stack[fromBox-1])-num:]
    stack[toBox-1] += arr2
    stack[fromBox-1]=arr
    print(stack)

    for num in range(0,num):
        ele = stack[fromBox-1].pop()
        stack[toBox-1].append(ele)
    print(stack)
    for i in stack:
        print(i[-1],end="")