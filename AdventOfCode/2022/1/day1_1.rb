file = File.open("day1_1.txt")
input_data = file.readlines.map(&:chomp)
result = 0
current = 0
for data in input_data
  if data.size == 0
    result = [result,current].max
    current = 0
  else
    current += data.to_i
  end 
end 
result = [result,current].max
puts result