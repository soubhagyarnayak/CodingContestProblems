require 'set'
file = File.open("day9_2.txt")
input_data = file.readlines.map(&:chomp)

h = [0,0]
t = []
n = 9
n.times {
    t.push([0,0])
}
positions = Set.new()
positions.add("0_0")

def find_next(h,t)
    nxt = [t[0],t[1]]
    if (h[0]==t[0] and h[1]==t[1]) or (h[0]==t[0] and (h[1]-t[1].abs==1)) or ((h[0]-t[0]).abs==1 and h[1]==t[1])
        nxt = [t[0],t[1]]
    elsif h[0]==t[0]+2 and h[1]==t[1]
        nxt[0] += 1
    elsif h[0]==t[0]-2 and h[1]==t[1]
        nxt[0] -= 1
    elsif h[1]==t[1]+2 and h[0]==t[0]
        nxt[1] += 1
    elsif h[1] == t[1]-2 and h[0]==t[0]
        nxt[1] -= 1
    elsif h[0]>t[0] and h[1]>t[1] and ((h[0]-t[0]).abs+(h[1]-t[1]).abs>2)
        nxt[0] += 1
        nxt[1] += 1
    elsif h[0]>t[0] and h[1]<t[1] and ((h[0]-t[0]).abs+(h[1]-t[1]).abs>2)
        nxt[0] += 1
        nxt[1] -= 1
    elsif h[0]<t[0] and h[1]<t[1] and ((h[0]-t[0]).abs+(h[1]-t[1]).abs>2)
        nxt[0] -= 1
        nxt[1] -= 1 
    elsif h[0]<t[0] and h[1]>t[1] and ((h[0]-t[0]).abs+(h[1]-t[1]).abs>2)
        nxt[0] -= 1
        nxt[1] += 1
    end 
    nxt 
end 

def find_next_t(h,t,positions,n)
    head = h 
    for i in (0...n)
        nxt = find_next(head,t[i])
        t[i] = nxt
        head = t[i] 
    end
    positions.add("#{t[-1][0]}_#{t[-1][1]}")
end 


for line in input_data
    parts = line.split(/ /)
    range = parts[1].to_i
    if parts[0]=='R'
        for i in (1..range)
            h[0] += 1
            find_next_t(h,t,positions,n)
        end 
    elsif parts[0]=='L'
        for i in (1..range)
            h[0] -= 1
            find_next_t(h,t,positions,n)
        end 
    elsif parts[0]=='U'
        for i in (1..range)
            h[1] += 1
            find_next_t(h,t,positions,n)
        end 
    else 
        for i in (1..range)
            h[1] -= 1
            find_next_t(h,t,positions,n)
        end 
    end 
end 

puts positions.size 