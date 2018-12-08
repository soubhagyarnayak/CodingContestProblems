def process_node(start,data):
    #print(start, data)
    num_nodes = int(data[start])
    num_metadata = int(data[start+1])
    start = start+2
    sum = 0
    for i in range(num_nodes):
        (start,sum1) = process_node(start,data)
        sum += sum1
    for i in range(num_metadata):
        sum += int(data[start+i])
    start += num_metadata
    #print(sum,start)
    return (start,sum)
 

f = open("./day8.txt")
lines = f.readlines()[0]
data = lines.split(' ')
print(process_node(0,data))

