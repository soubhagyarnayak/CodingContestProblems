file = File.open('day2_1.txt')
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
    y = mapper[line[2]]
    if x==y 
        score += 3 + y 
    elsif (x==1 and y==2) or (x==2 and y==3) or (x==3 and y==1)
        score += 6 + y 
    else 
        score += y 
    end 
end 
puts score 