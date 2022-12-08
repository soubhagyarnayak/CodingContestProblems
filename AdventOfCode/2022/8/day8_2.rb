file = File.open("day8_2.txt")
input_data = file.readlines.map(&:chomp)

data = []
for line in input_data
    data.push(line.chars.map(&:to_i))
end 

result = 0

def find_visibility(i,j,data)
    if i==0 or i==data.size-1 or j==0 or j==data[0].size-1
        return 0
    end 
    result = 1
    x = 0
    for row in (0...i).reverse_each
        x += 1
        break if data[row][j]>=data[i][j]
    end 
    result *= x
    
    x = 0
    for row in (i+1...data.size)
        x += 1
        break if data[row][j]>=data[i][j]
    end 
    result *= x

    y = 0
    for col in (0...j).reverse_each
        y += 1
        break if data[i][col]>=data[i][j] 
    end 
    result *= y
    
    y = 0
    for col in (j+1...data[0].size)
        y += 1
        break if data[i][col]>=data[i][j]
    end 
    result *= y 
    result
end 
    

for i in (0...data.size)
    for j in (0...data[0].size)
        score = find_visibility(i,j,data)
        result = [result,score].max
    end 
end 


puts result


