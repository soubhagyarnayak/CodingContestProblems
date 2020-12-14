package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main()  {
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
	if _, ok := mapper["byr"]; !ok {
		return false
	}
	if _, ok := mapper["iyr"]; !ok {
		return false
	}
	if _, ok := mapper["eyr"]; !ok {
		return false
	}
	if _, ok := mapper["hgt"]; !ok {
		return false
	}
	if _, ok := mapper["hcl"]; !ok {
		return false
	}
	if _, ok := mapper["ecl"]; !ok {
		return false
	}
	if _, ok := mapper["pid"]; !ok {
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

//ans is 233