def update(grid,entry,i,x_max,y_max):
    for x in range (x_max+1):
        for y in range (y_max+1):
            v = abs(entry[0]-x)+abs(entry[1]-y)
            if v < grid[y][x][0]:
                grid[y][x] = (v,i)
            elif v == grid[y][x][0] and v!=0:
                grid[y][x] = (v,-1)

def printg(grid,x_max,y_max):
    for i in range(y_max+1):
        s = []
        for j in range(x_max+1):
            c = str(grid[i][j][1])
            if grid[i][j][1] == -1:
                c = '*'
            s.append(c)
        print(' '.join(s))


f = open("./day6.txt")
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
value = x_max+y_max+3
grid = []
for i in range(y_max+1):
    line = []
    for j in range(x_max+1):
        line.append([value,-1])
    grid.append(line)
distance = []
for i in range(y_max+1):
    for j in range(x_max+1):
        k = 0
        for entry in entries:
            dist = (k,abs(i-entry[1])+abs(j-entry[0]))
            k += 1
            distance.append(dist)

        
'''
i = 0
for entry in entries:
    grid[entry[1]][entry[0]] = (0,i)
    i += 1
#printg(grid,x_max,y_max)
i = 0
for entry in entries:
    update(grid,entry,i,x_max,y_max)
    i += 1
dict = {}
for i in range(len(entries)):
    dict[i] = 0
for i in range(y_max+1):
    for j in range(x_max+1):
        if grid[i][j][1] != -1:
            dict[grid[i][j][1]] += 1
m = 0
for i in dict:
    print(i,dict[i])
    if m<dict[i]:
        m = dict[i]
print(x_min)
print(x_max)
print(y_min)
print(y_max)
print(len(entries))
print(m)
#printg(grid,x_max,y_max)
'''