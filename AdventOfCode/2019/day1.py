f = open("./day1.txt")
data = f.readlines()
#print(sum([(int(d)//3)-2 for d in data]))
s = 0
while True:
    data = [(int(d)//3)-2 for d in data]
    data = [d for d in data if d>0]
    if len(data)==0:
        break
    s += sum(data)
print(s)

