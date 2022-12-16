
file = open("day8.txt", "r").read().splitlines()
# file = open("sample.txt", "r").read().splitlines()
# print(file)


sum = 392  # 392
# print(ele)
arr = []

c = 0
for i in range(1, 98):
    for j in range(1, 98):
        ele = file[i][j]
        rightside = file[i][j+1:]
        mxr = max(rightside)

        if (ele > mxr):
            sum += 1
        else:
            leftside = file[i][:j]
            mxl = max(leftside)
            if (ele > mxl):
                sum += 1

            else:
                f = 0
                for x in range(0, i):
                    topVal = file[x][j]
                    if (ele <= topVal):
                        f = 1
                        break

                if f == 0:
                    sum += 1

                else:
                    f1 = 0
                    for y in range(i+1, 99):
                        botVal = file[y][j]
                        if (ele <= botVal):
                            f1 = 1
                    if f1 == 0:
                        sum += 1
# print(sum)


sc=0
for i in range(1,98):
    for j in range(1,98):
        ele = file[i][j]
        r,l,t,b =0,0,0,0
        rList = file[i][j+1:]
        for k in rList:
            if(ele>k):
                r+=1
            else:
                r+=1
                break
        lList = file[i][:j]
        for pp in lList[::-1]:
            if(ele>pp):
                l+=1
            else:
                l+=1
                break
        
        for x in range(i-1,-1,-1):
            val = file[x][j]
            if(ele>val):
                t+=1
            else:
                t+=1
                break

        for y in range(i+1,99):
            val = file[y][j]
            if(ele>val):
                b+=1
            else:
                b+=1
                break
        if(sc<l*r*t*b):
            sc = l*r*t*b
print(sc)
    

        
        

        
        
        
        


        
