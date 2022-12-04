input = open("input3.txt", "r")
data = input.read()
val = data.splitlines()
sum = 0
for i in val:
    x = (i[0:int(len(i)/2)])
    y = (i[int(len(i)/2):])
    

    arr = []
   
    for j in x:
        if j in y:
            arr.append(j)
    lett = arr[0]
    if lett.islower():
        value = ord(lett)-96
    else:
        value = ord(lett)-38
    sum= sum+value
    print(sum)


badgeSum = 0
N = 3
list = [val[n:n+N] for n in range(0, len(val), N)]
# print(list)

for i in list:
    arr = []  
    x = i[0]
    y = i[1]
    z = i[2]
    # for j in x:
    #     if j in y:
    #         if j in z:
    #             arr.append(j)
    for j in x:
        if ((j in y) and (j in z)):
                arr.append(j)
    badge = arr[0]
    print(badge)

    if badge.islower():
        value = ord(badge)-96
    else:
        value = ord(badge)-38
    badgeSum = badgeSum+value
    print(badgeSum)


       