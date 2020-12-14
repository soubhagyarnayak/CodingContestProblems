package main

import (
	"bufio"
	"fmt"
	"os"
    "strconv"
	"strings"
)

func main() {
	lines,err := readInput()
	if err!=nil {
		fmt.Println(err)
		return
	}
	mapper := make(map[string]string)
	result := 0
	for _,line := range(lines) {
		if len(line) != 0 {
			parts := strings.Split(line, " ")
			for _,part := range(parts){
				subs := strings.Split(part, ":")
				if(len(subs)>1){
					mapper[subs[0]] = subs[1]
				}
			}
		} else {
			if isValid(mapper) {
				result += 1
			}
			mapper = make(map[string]string)
		}
	}
	if isValid(mapper) {
		result += 1
	}
	fmt.Println(result)
}

func isValid(mapper map[string]string) bool {
	if val, ok := mapper["byr"]; ok {
		num, err := strconv.Atoi(val)
        if err!=nil {
            return false
        }
        if num <1920 || num >2002 {
            return false
        }
	} else {
        return false
    }
	if val, ok := mapper["iyr"]; ok {
		num, err := strconv.Atoi(val)
        if err!=nil {
            return false
        }
        if num < 2010 || num > 2020 {
            return false
        }
	} else {
        return false
    }
	if val, ok := mapper["eyr"]; ok {
		num, err := strconv.Atoi(val)
        if err!=nil {
            return false
        }
        if num <2020 || num >2030 {
            return false
        }
	} else {
        return false
    }
	if val, ok := mapper["hgt"]; ok {
		suffix := val[len(val)-2:]
        prefix := val[:len(val)-2]
        value,_ := strconv.Atoi(prefix)
        if suffix== "cm" {
             if value <150 || value>193 {
                 return false
             }
        } else if suffix =="in"{
            if value <59 || value>76 {
                 return false
            }
        } else {
            return false
        }
	} else {
        return false
    }
	if val, ok := mapper["hcl"]; ok {
		if val[:1] != "#" {
            return false
        }
        for i:=1; i<len(val); i++ {
            if !((val[i]>='0' && val[i]<='9')||(val[i]>='a' && val[i]<='f')){
                return false
            }
        }
	} else {
        return false
    }
	if val, ok := mapper["ecl"]; ok {
		if val != "amb" && val!="blu" && val!="brn" && val!="gry" && val!="grn" && val!="hzl" && val!="oth" {
            return false
        }
	} else {
        return false
    }
	if val, ok := mapper["pid"]; ok {
		if len(val)!=9 {
            return false
        }
	} else {
        return false
    }
	return true
}

func readInput() ([]string, error) {
	var lines = make([]string, 0)

	file, err := os.Open("./day4.txt")
	if err!=nil {
		return lines, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, nil
}

//ans is 111