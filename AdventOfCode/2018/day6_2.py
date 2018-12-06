f = open("./input6.txt")
lines = f.readlines()
entries = []
for line in lines:
    xy = line.split(', ')
    entries.append((int(xy[0]),int(xy[1])))
x_min = entries[0][0] 
x_max = entries[0][0]
y_min = entries[0][1] 
y_max = entries[0][1] 
for entry in entries:
    if x_min > entry[0]:
        x_min = entry[0]
    if x_max < entry[0]:
        x_max = entry[0]
    if y_min > entry[1]:
        y_min = entry[1]
    if y_max < entry[1]:
        y_max = entry[1]
count = 0
for i in range(x_max+1):
    for j in range(y_max+1):
        dist = 0
        for entry in entries:
            dist += abs(entry[0]-i)+abs(entry[1]-j)
            if dist>10000:
                break
        if dist<10000:
            count += 1
print(count)