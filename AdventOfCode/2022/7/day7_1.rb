file = File.open("day7_1.txt")
input_data = file.readlines.map(&:chomp)

fs_dir = Hash.new { |h, k| h[k] = [] }
fs_files = Hash.new { |h, k| h[k] = [] }
sizes = {}
path = []
abs_path = ""
max_size = 0
for line in input_data
  if line.start_with?("$ cd")
    dir = line[5...line.size]
    if dir==".."
      path.pop()
      abs_path = path.join("/")
    elsif dir!="."
      path.push(dir)
      abs_path = path.join("/")
    end  
    if path.size>max_size 
        puts abs_path
        max_size = path.size
    end
  elsif line.start_with?("dir ")
    dir_name = line[4...line.size]
    fs_dir[abs_path].push(abs_path+"/"+dir_name)
  elsif line!="$ ls" 
    parts = line.split(/ /)
    file_path = "#{abs_path}/#{parts[0]}"
    sizes[file_path] = parts[0]
    fs_files[abs_path].push(file_path)
  end 
end 

dir_sizes = {}
def find_size(dir_name, dir_sizes, fs_dir, fs_files, sizes, counter)
    puts "#{counter}: #{dir_name}"
    if dir_sizes.key?(dir_name)
        return dir_sizes[dir_name]
    end
    result = 0
    for child_dir in fs_dir[dir_name]
        result += find_size(child_dir, dir_sizes, fs_dir, fs_files, sizes, counter+1)
    end 
    for file in fs_files[dir_name]
        result += sizes[file].to_i
    end 
    dir_sizes[dir_name] = result
    return result
end 
find_size("/", dir_sizes, fs_dir, fs_files, sizes,0)


#puts fs_dir.inspect
#puts fs_files.inspect 
#puts sizes.inspect 
#puts dir_sizes.inspect

result = 0
dir_sizes.each do |key,value|
    result += value if value<=100000
end 
puts result 

