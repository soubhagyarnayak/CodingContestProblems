f = open("./day2.txt")
data = f.readlines()[0].split(',')
data = [int(d) for d in data]

data[1] = 12
data[2] = 2

i = 0
while True:
    opcode = data[i]
    if opcode == 1:
        val1 = data[data[i+1]]
        val2 = data[data[i+2]]
        data[data[i+3]]=val1+val2
        i += 4
    elif opcode == 2:
        val1 = data[data[i+1]]
        val2 = data[data[i+2]]
        data[data[i+3]]=val1*val2
        i += 4
    elif opcode == 99:
        break

print(data[0])