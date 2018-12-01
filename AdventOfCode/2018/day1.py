f = open("./day1.txt")
data = f.readlines()
result = 0
freqs = {}
input = []
for d in data:
    input.append(int(d))
found = False
while True:
    for d in input:
        result += d
        if result in freqs:
            print(result)
            found = True
            break
        else:
            freqs[result]=1
    if found:
        break
print(result)