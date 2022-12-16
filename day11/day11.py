test = open("inp.txt", "r").readlines()
# test = open("sampl.txt", "r").readlines()
# print(test)

from itertools import islice
split_len = [6,1,6,1,6,1,6,1,6,1,6,1,6,1,6]
data = iter(test) 
nlist = [list(islice(data,ele)) for ele in split_len]
# print(nlist)



m0 = [74, 64, 74, 63, 53]
m1 = [69, 99, 95, 62]
m2 = [59, 81]
m3 = [50, 67, 63, 57, 63, 83, 97]
m4 = [61, 94, 85, 52, 81, 90, 94, 70]
m5 = [69]
m6 = [54, 55, 58]
m7 = [79, 51, 83, 88, 93, 76]

monkeys=[]

for i in nlist:
    if i != ['\n']:
        # print(i)
        m=[]
        m.append(list(map(int,i[1].split(":")[1].split(","))))
        m.append(eval("lambda old:"+i[2].split("=")[1]))
        for j in i[3:]:
            m.append(int(j.split()[-1]))    
        monkeys.append(m)        

round=[0]* len(monkeys)

for _ in range(20):
    for index,m in enumerate(monkeys):
        for item in m[0]:
            item = m[1](item)
            item //=3
            if item%m[2] ==0:
                monkeys[m[3]][0].append(item)
            else:
                monkeys[m[4]][0].append(item)
        round[index]+=len(m[0])
        m[0]=[]

round.sort()
print(round[-1]*round[-2])