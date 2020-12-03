package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main(){
	lines,err := readInput()
	if err!=nil {
		fmt.Println(err)
		return
	}
	result := 0
	for _,line := range(lines) {
		parts := strings.Split(line, ":")
		subs := strings.Split(parts[0]," ")
		nums := strings.Split(subs[0],"-")
		pos1,_ := strconv.Atoi(nums[0])
		pos2,_ := strconv.Atoi(nums[1])
		t1 := parts[1][pos1]==subs[1][0]
		t2 := parts[1][pos2]==subs[1][0]
		if t1!=t2 {
			result += 1
		}
	}
	fmt.Println(result)
}

func readInput() ([]string, error) {
	var lines = make([]string, 0)

	file, err := os.Open("./day2_2.txt")
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

// ans for part 1 is 383