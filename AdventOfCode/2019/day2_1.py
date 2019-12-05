f = open("./day2_1.txt")
input = f.readlines()[0].split(',')
input = [int(d) for d in input]

for noun in range(100):
    for verb in range(100):
        data = input[:]
        data[1] = noun
        data[2] = verb

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
        if data[0] == 19690720:
            print(100*noun+verb)
            break