package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func main() {
	nums, err := readInput()
	if err!=nil {
		fmt.Println(err)
	}
	sort.Ints(nums)
	for i:=0; i<(len(nums)-2);i++ {
		complement := 2020-nums[i]
		left := i+1
		right := len(nums)-1
		for left<right {
			sum := nums[left]+nums[right]
			if sum==complement {
				fmt.Println(nums[i]*nums[left]*nums[right])
				return
			} else if sum<complement {
				left += 1
			} else {
				right -= 1
			}
		}
	}
}

func readInput() ([]int,error) {
	var nums = make([]int, 0)

	file, err := os.Open("./day1_2.txt")
	if err!=nil {
		return nums, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Split(bufio.ScanLines)

	for scanner.Scan() {
		num,err := strconv.Atoi(scanner.Text())
		if err!= nil {
			return nums, err
		} 
		nums = append(nums,num)
	}
	return nums, nil
}

//ans 246191688