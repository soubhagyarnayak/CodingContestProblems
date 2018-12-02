f = open("./day2.txt")
entries = f.readlines()
c1 = 0
c2 = 0
candidates = []
for entry in entries:
    map = {}
    for c in entry:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
    found1 = False
    found2 = False
    found3 = False
    found4 = False
    for key in map:
        if map[key]==2:
            if found1:
                found2 = True
            else:
                found1= True
        elif map[key]==3:
            if found3:
                found4 = True
            else:
                found3 = True
    if found1:
        c1 += 1
    if found3:
        c2 += 1
    if found1 or found3:
        candidates.append(entry)
print(c1)
print(c2)
print(c1*c2)
result = []
for candidate in candidates:
    for candidate2 in candidates:
        found = 0
        if candidate == candidate2:
            continue
        for i in range (len(candidate)):
            if candidate[i]!=candidate2[i]:
                found += 1
            if found > 1:
                break
        if found == 1:
            result.append(candidate)
for f in result:
    print(f)
        
