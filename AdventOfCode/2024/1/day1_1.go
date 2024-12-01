package main

import (
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func main() {
	//solve1()
	solve2()
}

func solve1() {
	data, err := os.ReadFile("./day1_2.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	lines := strings.Split(string(data), "\n")
	var a, b []int
	for _, line := range lines {
		entries := strings.Split(line, "   ")
		first, err := strconv.Atoi(entries[0])
		if err != nil {
			fmt.Println(err)
			return
		}
		second, err := strconv.Atoi(entries[1])
		if err != nil {
			fmt.Println(err)
			return
		}
		a = append(a, first)
		b = append(b, second)
	}
	sort.Ints(a)
	sort.Ints(b)
	fmt.Println(a)
	fmt.Println(b)
	var result int
	for index, entry := range a {
		diff := entry - b[index]
		if diff < 0 {
			diff = -diff
		}
		fmt.Println(diff)
		result += diff
	}
	fmt.Println(result)
}

func solve2() {
	data, err := os.ReadFile("./day1_2.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	lines := strings.Split(string(data), "\n")
	var a []int
	b := make(map[int]int)
	for _, line := range lines {
		entries := strings.Split(line, "   ")
		first, err := strconv.Atoi(entries[0])
		if err != nil {
			fmt.Println(err)
			return
		}
		a = append(a, first)
		second, err := strconv.Atoi(entries[1])
		if err != nil {
			fmt.Println(err)
			return
		}
		b[second] += 1
	}
	fmt.Println(a)
	fmt.Println(b)
	var result int
	for _, entry := range a {
		result += entry * b[entry]
	}
	fmt.Println(result)
}
