require 'set'

file = File.open("day3_2.txt")
input_data = file.readlines.map(&:chomp)
result = 0
i = 0
while i<input_data.length
    first = Set.new(input_data[i].chars)
    second = Set.new(input_data[i+1].chars)
    third = Set.new(input_data[i+2].chars)
    i += 3
    common = first & second & third 
    for c in common
        result += c.ord-'A'.ord+27 if c.ord<='Z'.ord
        result += c.ord-'a'.ord+1 if c.ord>'Z'.ord
    end
end 
puts result