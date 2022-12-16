file = open("input9.txt", "r").read()
# file = open("sample.txt", "r").read()
data = file.splitlines()
# print(data)
# print(data[1][0])
    # print( dir,step)
row_dir = {"R":1, "L":-1, "U":0, "D":0}
col_dir = {"R":0, "L":0, "U":-1, "D":1}
H = (0,0)
T1 = (0,0)
T = ((0,0) for i in range(9))

def findTail(H,T):
    col = (H[0]-T[0])
    row = (H[1]-T[1])
    if abs(row) <= 1 and abs(col) <= 1:
        pass
    elif abs(row) >= 2 and abs(col) >= 2:
        if T[0] < H[0]:
            if T[1] < H[1]:
                T = (H[0]-1, H[1]-1)
            else:
                T = (H[0]-1, H[1]+1)
        else:
            if T[1] < H[1]:
                T = (H[0]+1, H[1]-1)
            else:
                T = (H[0]+1, H[1]+1)
    elif abs(col) >= 2:
        if T[0] < H[0]:
            T = (H[0]-1, H[1])
        else:
            T = (H[0]+1, H[1])
    elif abs(row) >= 2:
       if T[1] < H[1]:
           T = (H[0], H[1]-1)
       else:
           T = (H[0], H[1]+1)
    return T


traversal1 = set()
for x in data:
    dir = x[0]
    step = int(x[-1])
    for y in range(step):
        traversal1.add(T1)
        H = (H[0]+col_dir[dir],H[1]+row_dir[dir])
        T1 = findTail(H,T1)
    traversal1.add(T1)


H = (0, 0)
traversal2 = set()
for line in data:
    s1, s2 = line.split(' ')
    # print(s1,s2)
    s2 = int(s2)
    for z in range(s2):
        traversal2.add(T[8])
        H = (H[0]+col_dir[s1], H[1]+row_dir[s1])
        T[0] = findTail(H, T[0])
        for i in range(1, 9):
            T[i] = findTail(T[i-1], T[i])
        traversal2.add(T[8])

print(len(traversal1))
print(len(traversal2))
    

    
























  
    # i = -1
    # j = 0
    # curr = mat[i][j]
    # # print("ipo", curr)
    # if dir == "R":
    #     Hpos = mat[i][j+step]
    #     Tpos = mat[i][j+(step-1)]
    #     curr = Hpos
    #     Tpos = "#"
    #     # print("after move", curr)
    # elif dir == "L":
    #     Hpos = mat[i][j-step]
    #     Tpos = mat[i][j-(step+1)]
    #     curr = Hpos
    #     Tpos = "#"
    # elif dir == "U":
    #     Hpos = mat[i+step][j]
    #     Tpos = mat[i+(step-1)][j]
    #     curr = Hpos
    #     Tpos = "#"
    # elif dir == "D":
    #     Hpos = mat[i-step][j]
    #     Tpos = mat[i-(step-1)][j]
    #     curr = Hpos
    #     Tpos = "#"
    # print(curr)
