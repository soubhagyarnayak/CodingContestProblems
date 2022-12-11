file = File.open("day10_2.txt")
input_data = file.readlines.map(&:chomp)
t = 0
v = 1
signals = []
def update_signals(t,v,signals)
    if t==20 or t==60 or t==100 or t==140 or t==180 or t==220
        signal = t*v 
        signals.push(signal)
        puts "#{t}-#{v}-#{signal}"
    end
end 
for line in input_data
    if line=="noop"
        t += 1
        update_signals(t,v,signals)
    else 
        parts = line.split(/ /)
        val = parts[1].to_i 
        t += 1
        update_signals(t,v,signals)
        t += 1
        update_signals(t,v,signals)
        v += val
    end
end  

puts signals.inspect
puts signals.sum