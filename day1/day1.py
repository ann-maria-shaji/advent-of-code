array = []
sum = 0
nfile = open("txt1.txt", "r")
data = nfile.read()
num=(data.splitlines())
# print(num)
for i in num:
    if (i==''):
        array.append(sum)
        sum = 0
    else:
        sum = sum +int(i)

print(max(array)) #highest calorie
array.sort()
print(array) 

    
        


