use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    const RADIX: u32 = 10;
    let mut result = 0;
    if let Ok(lines) = read_lines("./day1_1.txt") {
        for line in lines {
            if let Ok(str) = line {
                let mut first = 0;
                let mut last = 0;
                let mut is_set = false;
                for c in str.chars() {
                    if c.is_digit(RADIX) {
                        last = c.to_digit(RADIX).unwrap();
                        if !is_set {
                            first = last;
                            is_set = true;
                        }
                    }
                }
                result += first*10+last;
            }
        }
    }
    println!("{}",result)
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}