file = File.open('day2_2.txt')
input_data = file.readlines.map(&:chomp)
mapper = {
    'A' => 1,
    'B' => 2,
    'C' => 3,
    'X' => 1,
    'Y' => 2,
    'Z' => 3,
}
score = 0
for line in input_data
    x = mapper[line[0]]
    y = line[2]
    if y=='X'
        if x==1
           score += 3
        elsif x==2
            score += 1
        elsif x==3
            score += 2
        end      
    elsif y=='Y'
        score += 3 + x 
    else 
        if x==1
            score += 6+2
         elsif x==2
             score += 6+3
         elsif x==3
             score += 6+1
         end
    end 
end 
puts score 