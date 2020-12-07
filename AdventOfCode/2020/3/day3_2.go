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
	result := 1
	result *= findTrees(lines,1,1)
	result *= findTrees(lines,1,3)
	result *= findTrees(lines,1,5)
	result *= findTrees(lines,1,7)
	result *= findTrees(lines,2,1)

	fmt.Println(result)
}

func findTrees(lines []string, downJumpStep int, rightJumpStep int)(int) {
	count := 0
	for i:=1; (i*downJumpStep)<len(lines); i++ {
		c := lines[i*downJumpStep][(rightJumpStep*i)%len(lines[0])]
		if c=='#' {
			count += 1
		}
	}
	return count
}

func readInput() ([]string, error) {
	var lines = make([]string, 0)

	file, err := os.Open("./day3_2.txt")
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

// ans is 1592662500