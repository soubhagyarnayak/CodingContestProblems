file = File.open("day4_2.txt")
input_data = file.readlines.map(&:chomp)
result = 0
for line in input_data
    parts = line.split(/[,-]/).map(&:to_i)
    if (parts[0]<=parts[2] and parts[2]<=parts[1]) or (parts[0]<=parts[3] and parts[3]<=parts[1]) or (parts[2]<=parts[0] and parts[0]<=parts[3]) or (parts[2]<=parts[1] and parts[1]<=parts[3])
        result += 1
    end 
end 
puts result