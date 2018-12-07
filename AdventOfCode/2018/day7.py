import heapq
f = open("./day7.txt")
lines = f.readlines()
dict = {}
dict2 = {}
for line in lines:
    data = line.split(' must be finished before step ')
    first = data[0][-1]
    second = data[1][0]
    if first not in dict:
        dict[first] = []
    dict[first].append(second)
    if second not in dict2:
        dict2[second] = []
    dict2[second].append(first)
    if first not in dict2:
        dict2[first] = []
l = [] 
for key in dict:
    print("{}->{}".format(key,dict[key]))
print("-------------")
for key in dict2:
    print("{}->{}".format(key,dict2[key]))
o = []
m = len(dict2)
while True:
    if len(o) == m:
        break
    l1 = []
    for key in dict2:
        if len(dict2[key])==0:
            l1.append(key)
    for item in l1:
        dict2.pop(item)
        l.append(item)
    l = sorted(l)
    print(l)
    node = l[0]
    l.remove(node)
    if node in o:
        continue
    print(node)
    o.append(node)
    if node in dict:
        t = dict[node]
        for t1 in t:
            dict2[t1].remove(node)

print(''.join(o)) #JKNSTHCBGRVDXWAYFOQLMPZIUE


