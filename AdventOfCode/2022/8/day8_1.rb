file = File.open("day8_2.txt")
input_data = file.readlines.map(&:chomp)

data = []
for line in input_data
    data.push(line.chars.map(&:to_i))
end 

result = 0

visited = arr1 = Array.new(data.size) { Array.new(data[0].size){0}}

for i in (0...data.size)
    visited[i][0] = 1
    max = data[i][0]
    for j in (1...data[0].size-1)
        if data[i][j]>max
            visited[i][j] = 1
            max = data[i][j]
        end 
    end
    visited[i][-1] = 1
    max = data[i][-1]
    for j in (1...data[0].size-1).reverse_each
        if data[i][j]>max 
            visited[i][j] = 1
            max = data[i][j]
        end 
    end 
end 

for j in (0...data[0].size)
    visited[0][j] = 1
    max = data[0][j]
    for i in (1...data.size-1)
        if data[i][j]>max
            visited[i][j] = 1
            max = data[i][j]
        end 
    end 
    max = data[-1][j]
    visited[-1][j] = 1
    for i in (1...data.size-1).reverse_each
        if data[i][j]>max 
            visited[i][j] = 1
            max = data[i][j]
        end 
    end 
end 

for i in (0...visited.size)
    for j in (0...visited[0].size)
        result += visited[i][j]
    end 
end 

puts result
