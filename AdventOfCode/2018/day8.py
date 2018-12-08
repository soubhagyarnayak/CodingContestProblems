class Node:
    def __init__(self,start):
        self.nodes = []
        self.metadata = []
        self.start = start
        print(start)
    def value(self):
        val = 0
        if len(self.nodes)==0:
            #print("empty"+str(self.start)+str(len(self.nodes)))
            for m in self.metadata:
                val += m
        else:
            #print("index"+str(self.start)+":"+str(len(self.nodes)))
            for m in self.metadata:
                if m <= len(self.nodes):
                    val += self.nodes[m-1].value()
        print(val)
        return val
def process_node(start,data):
    #print(start, data)
    node = Node(start)
    num_nodes = int(data[start])
    num_metadata = int(data[start+1])
    start = start+2
    sum = 0
    for i in range(num_nodes):
        (childnode,start,sum1) = process_node(start,data)
        node.nodes.append(childnode)
        sum += sum1
    for i in range(num_metadata):
        sum += int(data[start+i])
        node.metadata.append(int(data[start+i]))
    start += num_metadata
    #print(sum,start)
    return (node,start,sum)
def printn(node,prefix):
    print(prefix + str(len(node.nodes))+ ":" + str(len(node.metadata)))
    meta = "meta: "
    for m in node.metadata:
        meta += str(m)+ " "
    print(prefix + meta)
    for cnode in node.nodes:
        printn(cnode,prefix+"\t")
    

f = open("./day8.txt")
lines = f.readlines()[0]
data = lines.split(' ')
(root,start,sum) = process_node(0,data)
print("result:")
print(root.value())
#printn(root,"")

