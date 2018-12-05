def reduce(entry):
    s = []
    for c in entry:
        if len(s)==0:
            s.append(c)
        elif abs(ord(s[-1])-ord(c))==32:
            s.pop()
        else:
            s.append(c)
    return len(s)

f = open("./day5.txt")
entry = f.readlines()[0]
min = reduce(entry)
print(min)