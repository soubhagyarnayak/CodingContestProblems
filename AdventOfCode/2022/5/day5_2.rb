file = File.open("day5_2.txt")
input_data = file.readlines.map(&:chomp)
data = []
for line in input_data
    next if line.size==0
    if line.start_with?("move")
        #move 1 from 2 to 1
        m = line.match(/\w+ (\d+) \w+ (\d+) \w+ (\d+)/)
        count = m[1].to_i 
        from = m[2].to_i-1
        to = m[3].to_i-1
        buffer = []
        count.times {
            buffer.unshift(data[from].shift)
        }
        count.times {
            data[to].unshift(buffer.shift)
        }

    elsif !line.start_with?(" 1")
        i = 1
        j = 0
        while i<line.size
            if j>=data.size 
                data.push([])
            end
            if line[i]!=' '
                data[j].push(line[i])
            end
            j += 1
            i += 4
        end 
    end
end
result = ""
for entry in data 
    result += entry[0] 
end  
puts result