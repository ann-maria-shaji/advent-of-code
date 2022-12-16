inp = open("input6.txt", "r").read()
# print(inp)
# print(len(inp))

for i in range(len(inp)-14):
    # print(i, inp[i])
    
    # if ( i!=(i+1) and(i+2) and (i+3)):
    # if(inp[i])
    # x = inp[i] and inp[i+1] and inp[i+2] and inp[i+3]
    # print(x)
    a = inp[i]
    b = inp[i+1]
    c = inp[i+2]
    d = inp[i+3]
    e = inp[i+4]
    f = inp[i+5]
    g= inp[i+6]
    h = inp[i+7]
    j = inp[i+8]
    k = inp[i+9]
    l = inp[i+10]
    m = inp[i+11]
    n = inp[i+12]
    o = inp[i+13]
    # p = inp[i+14]

    arr = [a,b,c,d,e,f,g,h,j,k,l,m,n,o]
    set1 = set(arr)
    if(len(set1)==14):
        print(set1)
        break
print(i+14)
  