package main

import "fmt"

func main() {

	a := make(map[string]string)
	// b := make(map[int]string)

	a["Name"] = "Karthi"
	a["age"] = "25"

	fmt.Println(a.keys())
}
