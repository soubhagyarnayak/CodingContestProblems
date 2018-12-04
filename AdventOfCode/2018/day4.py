def find_max_sleep(sleeptimes):
    minutes = {}
    for i in range (60):
        minutes[i] = 0
    for sleeptime in sleeptimes:
        for t in range(sleeptime[0],sleeptime[1]):
            minutes[t] += 1
    max_minute = 0
    max_value = 0
    for i in range(60):
        if minutes[i]>max_value:
            max_value = minutes[i]
            max_minute = i
    return (max_value,max_minute)
f = open("./day4.txt")
lines = f.readlines()
entries = []
for line in lines:
    parts = line.split(']')
    part0 = parts[0].split('[')[1]
    part1 = parts[1]
    date = part0.split(' ')[0]
    date = date.split('-')
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    time = part0.split(' ')[1]
    hour = int(time.split(':')[0])
    minute = int(time.split(':')[1])
    entry = (month,day,hour,minute,part1.strip())
    entries.append(entry)
entries = sorted(entries, key=lambda element: (element[0], element[1], element[2],element[3]))
guards = {}
guard = None
start = 0
end = 0
for entry in entries:
    if entry[4].startswith('Guard'):
        if start != 0:
            end = entry[3]
        if guard not in guards:
            guards[guard] = []
        guards[guard].append((start,end))
        start = 0
        end = 0
        guard = entry[4].split('Guard #')[1]
        #print(guard)
        guard = guard.split(' ')[0]
        #print(guard)
        guard = int(guard)
    elif entry[4].startswith('falls'):
        start = entry[3]
    elif entry[4].startswith('wakes'):
        end = entry[3]
        if guard not in guards:
            guards[guard] = []
        guards[guard].append((start,end))
        end = 0
        start = 0
    else:
        print("Error")
times = {}
for guard in guards:
    st = 0
    for sleeptime in guards[guard]:
        st += sleeptime[1]-sleeptime[0]
    times[guard]=st
g0 = None
tm = 0
for t in times:
    if times[t]>tm:
        g0 = t
        tm = times[t]
print(g0)
minutes = {}
for i in range (60):
    minutes[i] = 0
for sleeptime in guards[g0]:
    for t in range(sleeptime[0],sleeptime[1]):
        minutes[t] += 1
max_minute = 0
max_value = 0
for i in range(60):
    if minutes[i]>max_value:
        max_value = minutes[i]
        max_minute = i
print(max_minute)
print(g0*max_minute)
ggid = 0
ggmin = 0
gmax = 0
for guard in guards:
    (max,t) = find_max_sleep(guards[guard])
    if max > gmax:
        ggid = guard
        ggmin = t
        gmax = max
print(ggmin*ggid)
#print(len(guards))
#print(len(times))