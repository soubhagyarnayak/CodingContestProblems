from heapq import heappush, heappop


file = open("day1_2.txt")
input_data = file.readlines()
current = 0
pq = []
for data in input_data:
  data = data.strip('\n')
  if len(data) == 0:
    heappush(pq,-current)
    current = 0
  else:
    current += int(data)
heappush(pq,-current)
result = 0
for i in range(3):
  result += -heappop(pq)

print(result)