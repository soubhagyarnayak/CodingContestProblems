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
	count := 0
	for i:=1; i<len(lines); i++ {
		c := lines[i][(3*i)%len(lines[0])]
		if c=='#' {
			count += 1
		}
	}

	fmt.Println(count)
}

func readInput() ([]string, error) {
	var lines = make([]string, 0)

	file, err := os.Open("./day3.txt")
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

//ans is 250