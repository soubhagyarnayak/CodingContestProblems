require 'set'

file = File.open("day3_1.txt")
input_data = file.readlines.map(&:chomp)
result = 0
for line in input_data
    first = Set.new(line.chars[0,line.length/2])
    second = Set.new(line.chars[line.length/2,line.length])
    common = first & second
    for c in common
        result += c.ord-'A'.ord+27 if c.ord<='Z'.ord
        result += c.ord-'a'.ord+1 if c.ord>'Z'.ord
    end
end 
puts result