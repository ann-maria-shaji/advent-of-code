import re


file = open("input7.txt", "r").readlines()
# data = file.splitlines()
# print(file)


class rootNode:
    def __init__(self, root, size=0):
        self.root = root
        self.children = []
        self.parent = None
        self.size = size

    def print_tree(self):
        print(self.root)
        print(self.size)
        if self.children:
            for each in self.children:
                each.print_tree()


root = rootNode('/')
curr = root
tot = 0
for i in file:
    if i =="$":
        if i.startswith('$ cd'):
            if i[0:7] == '$ cd ..':
                curr = curr.parent
                pass
            else:
                x = i[5:]
                r = rootNode(x)
                r.parent = curr
                curr.children.append(r)
                curr = r
                # r.print_tree()
                # print(i)
    elif i=="$ ls":
        continue
    elif not i.startswith('dir'):
        s = re.findall('[0-9]+', i)
        if s != []:
            val = int(s[0])
            curr.children.append(rootNode(root, int(val)))
            # curr.print_tree()
            #     # print(val)
            #     if (val < 100000):
            #         # print(val)
            #         tot =tot + val
            #     print(tot)



def dfs(node):
    if not node.children:
        return node.size
    tot = 0
    for n in node.children:
        tot += dfs(n)
    return tot
dfs(root)
print(tot)
