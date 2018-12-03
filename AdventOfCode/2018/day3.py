f = open("./input3")
entries = f.readlines()
inputs = []
for entry in entries:
    datas = entry.split('@')
    id = int(datas[0].split('#')[1])
    ds = datas[1].split(':')
    d1s = ds[0].split(',')
    d2s = ds[1].split('x')
    x0 = int(d1s[0])
    y0 = int(d1s[1])
    dx = int(d2s[0])
    dy = int(d2s[1])
    xt = 2*x0+dx
    yt = 2*y0+dy
    inputs.append((x0,y0,dx,dy,xt,yt,id))
x_max = 0
y_max = 0
for input in inputs:
    x = input[4]
    y = input[5]
    if x>x_max:
        x_max = x
    if y>y_max:
        y_max = y

area = []
for y in range(y_max):
    l = []
    for x in range(x_max):
        l.append(0)
    area.append(l)
for input in inputs:
    for y in range(input[1],input[1]+input[3]):
        for x in range(input[0],input[0]+input[2]):
            area[y][x] += 1

result = 0
for y in range(y_max):
    for x in range(x_max):
        if area[y][x]>1:
            result += 1
print(result)
for input in inputs:
    found = True
    for y in range(input[1],input[1]+input[3]):
        for x in range(input[0],input[0]+input[2]):
            if area[y][x] > 1:
                found = False
                break
    if found:
        print(input[6])
        break