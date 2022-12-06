file = File.open('day6_1.txt')
line = file.readline()
counter = Hash.new(0)
for i in (0..3)
    counter[line[i].ord-'a'.ord] += 1
end 
for i in (4...line.length)
    if counter.values.any?{|x| x>1}
        counter[line[i].ord-'a'.ord] += 1
        counter[line[i-4].ord-'a'.ord] -= 1
    else
        puts i
        break
    end 
    
end 

            