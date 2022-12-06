file = File.open('day6_2.txt')
line = file.readline()
counter = Hash.new(0)
for i in (0..13)
    counter[line[i].ord-'a'.ord] += 1
end 
for i in (14...line.length)
    if counter.values.any?{|x| x>1}
        counter[line[i].ord-'a'.ord] += 1
        counter[line[i-14].ord-'a'.ord] -= 1
    else
        puts i
        break
    end     
end 
