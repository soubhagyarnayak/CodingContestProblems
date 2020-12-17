package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	lines,err := readInput()
	if err!=nil {
		fmt.Println(err)
		return
	}
	result := 0
	for _,line := range(lines) {
		score := getScore(line)
		if score>result {
			result = score
		}
	}
	fmt.Println(result)
}

func getScore(line string) int {
	low := 0
	high := 127
	for i:=0;i<7;i++ {
		if line[i]=='F' {
			high = high - (high-low+1)/2
		} else {
			low = low + (high-low+1)/2
		}
	}
	left := 0
	right := 7
	for i:=0; i<3; i++{
		if line[7+i]=='L'{
			right = right-(right-left+1)/2
		} else {
			left = left + (right-left+1)/2
		}
	}
	return 8*low+left
}

func readInput() ([]string, error) {
	var lines = make([]string, 0)

	file, err := os.Open("./day5.txt")
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

//ans is 913