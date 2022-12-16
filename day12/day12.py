test = open("inp.txt", "r").read()
# test = open("sam.txt", "r").read()
data = test.split("\n")
# print(data)


class Graph:

    graph_dict = {}

    def addEdge(self, node, neighbour):
        if node not in self.graph_dict:
            self.graph_dict[node] = [neighbour]
        else:
            self.graph_dict[node].append(neighbour)

    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(", node, "->", neighbour, ")")

    def show_graph(self):
        return self.graph_dict


def BFS_SP(graph, start, end):
    explored = []

    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]

    # If the desired node is
    # reached
    if start == end:
        print("Same Node")
        return

    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1]

        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]

            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

                # Condition to check if the
                # neighbour node is the goal
                if neighbour == end:
                    print("loading...")
                    return new_path
            explored.append(node)

    # Condition when the nodes
    # are not connected
    print("connecting path doesn't exist")
    return

graph = Graph()

for i in range(len(data)):
    data[i] = data[i].replace("S","a")
    data[i] = data[i].replace("E","z")

for i in range(len(data)):
    for j in range(len(data[i])):
        item = (i,j,data[i][j])
        if((i-1)>=0):
            if((ord(data[i][j])+1)>=ord(data[i-1][j])):
                top = (i-1,j,data[i-1][j])
                graph.addEdge(str(item),str(top))
        if((j-1)>=0):
            if ((ord(data[i][j])+1) >= ord(data[i][j-1])):
                left = (i, j-1, data[i][j-1])
                graph.addEdge(str(item), str(left))
        if((i+1)<len(data)):
            if ((ord(data[i][j])+1)>=ord(data[i+1][j])):
                bott = (i+1,j,data[i+1][j])
                graph.addEdge(str(item),str(bott))
        if((j+1)<len(data[i])):
            if ((ord(data[i][j])+1)>=ord(data[i][j+1])):
                right = (i, j+1, data[i][j+1])
                graph.addEdge(str(item),str(right))

def shortest():
    gr = graph.show_graph()
    # print(gr)
    # print(len(gr))
    spath = BFS_SP(gr,"(20, 0, 'a')", "(20, 112, 'z')")
    print(len(spath)-1)
shortest()

# def shortest2():
#     gr = graph.show_graph()
#     path_a = []
#     print(path_a)
#     for i in gr.keys():
#         if(i[-3]=='a'):
#             spath2 = BFS_SP(gr,i,"(20,112,'z')")
#             if(spath2):
#                 path_a.append(len(spath2)-1)
#     print(min(path_a))
# shortest2()


def part2():
    gr = graph.show_graph()
    path_a = []
    for i in gr.keys():
        if (i[-3] == "a"):
            spath = BFS_SP(gr, i, "(20, 112, 'z')")
            if (spath):
                path_a.append(len(spath)-1)
    print(min(path_a))
part2()
