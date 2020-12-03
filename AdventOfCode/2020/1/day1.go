package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	file, err := os.Open("./day1.txt")
	if err!=nil {
		fmt.Println(err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	var nums = make(map[int]bool)

	for scanner.Scan() {
		num,err := strconv.Atoi(scanner.Text())
		if err!= nil {
			fmt.Println(err)
			return
		}
		if _, ok := nums[2020-num]; ok {
			fmt.Println(num*(2020-num))
		} 
		nums[num] = true
	}
}

// expected ans for the input is 646779