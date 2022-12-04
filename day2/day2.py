inputfile = open("input2.txt", "r")
data = inputfile.read()
val  = (data.splitlines())
# print(val)


loss = 0
draw = 3
win = 6
sum = 0

for i in val:
    if (i == 'A X'):
     res = 3 + loss
   

    elif(i=='A Y'):
        res = 1 + draw

    elif(i=='A Z'):
        res = 2 + win
     
    elif(i =='B X'):
        res = 1 + loss

    elif( i == 'B Y'):
        res = 2 + draw

    
    elif(i == 'B Z'):
        res = 3 + win
        

    elif(i == 'C X'):
        res = 2 + loss

    elif(i == 'C Y'):
        res  = 3 + draw

    elif(i == 'C Z'):
        res = 1 + win
    sum = sum + res 

print(sum)
