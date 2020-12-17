package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	lines,err := readInput()
	if err!=nil {
		fmt.Println(err)
		return
	}
	scores := make([]int,0,1000)
	for _,line := range(lines) {
		score := getScore(line)
		scores = append(scores,score)
	}
	sort.Ints(scores)
	for i:=1;i<len(scores);i++ {
		if(scores[i]!=(scores[i-1]+1)){
			fmt.Println(scores[i-1]+1)
		}
	}
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

	file, err := os.Open("./day5_1.txt")
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

//ans is 717