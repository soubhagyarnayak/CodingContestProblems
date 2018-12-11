def plot(particles):
    x_start = particles[0][0]
    x_end = 0
    y_start = particles[0][1]
    y_end = 0
    for particle in particles:
        x_start = min(x_start,particle[0])
        x_end = max(x_end,particle[0])
        y_start = min(y_start,particle[1])
        y_end = max(y_end,particle[1])
    print(x_start,x_end,y_start,y_end)
    canvas = []
    for y in range(y_start,y_end+1):
        line = []
        for x in range(x_start,x_end+1):
            line.append('.')
        canvas.append(line)
    for particle in particles:
        canvas[particle[1]-y_start][particle[0]-x_start] = '*'
    for line in canvas:
        print(' '.join(line))

f = open("./day9.txt")
lines = f.readlines()
particles = []
for line in lines:
    data = line.split('>')
    data0 = data[0].split('<')[1]
    data1 = data[1].split('<')[1]
    data0 = data0.split(',')
    x = int(data0[0])
    y = int(data0[1])
    data1 = data1.split(',')
    dx = int(data1[0])
    dy = int(data1[1])
    particles.append((x,y,dx,dy))
time = 0
while True:
    particles = [(particle[0]+particle[2],particle[1]+particle[3],particle[2],particle[3]) for particle in particles]
    xlist = [particle[0] for particle in particles]
    countX = len(xlist)-len(set(xlist))
    ylist = [particle[1] for particle in particles]
    countY = len(ylist)- len(set(ylist))
    print(countX,countY,len(xlist),len(ylist))
    print(max(xlist)-min(xlist))
    time += 1
    if max(xlist)-min(xlist) <= 65:
        break
plot(particles)
print(time)
