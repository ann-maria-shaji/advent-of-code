import re
file = open("input4.txt", "r")
data = file.read()
val = data.splitlines()
sum = 0

for i in val:
    if( i != '-'):
        aString = i
        y = aString.split(",")
        sNum = (y[0])
        fNum = (y[1])
           
        z = re.findall('[0-9]+',sNum)
        b = re.findall('[0-9]+', fNum)
        c = int(z[0])
        d = int(z[1])
        e = int(b[0])
        f=int(b[1])
        # print(c,d,e,f)

        if (c<=e and d>=f) or (c>=e and d<=f):
            print(c,d)
            print(e,f)
            sum = sum+1
            print(sum)

        arr1 = []
        arr2=[]
        for x in range(c,d+1):
            arr1.append(x)
        # print(arr1)
        for n in range(e,f+1):
            arr2.append(n)
        # print(arr2)
        
        if any(item in arr1 for item in arr2):
            sum = sum+1
            print(sum)
        