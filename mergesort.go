package main

import (
	"fmt"
	"math/rand"
	"time"
)

// Merge Sort function
func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right []int) []int {
	result := []int{}
	i, j := 0, 0

	for i < len(left) && j < len(right) {
		if left[i] < right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	result = append(result, left[i:]...)
	result = append(result, right[j:]...)

	return result
}

func main() {
	// Test the sorting algorithm and measure execution time
	inputSize := 1000000
	arr := make([]int, inputSize)
	for i := 0; i < inputSize; i++ {
		arr[i] = rand.Intn(1000)
	}

	startTime := time.Now()
	mergeSort(arr)
	endTime := time.Now()

	fmt.Printf("Merge Sort execution time for %d elements: %v seconds\n", inputSize, endTime.Sub(startTime).Seconds())
}
