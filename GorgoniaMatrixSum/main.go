package main

import (
	"fmt"
	"log"

	. "gorgonia.org/gorgonia"
	"gorgonia.org/tensor"
)

func main() {
	g := NewGraph()

	a := tensor.New(tensor.WithShape(2, 2), tensor.WithBacking([]float32{1, 2, 3, 4}))
	b := tensor.New(tensor.WithShape(2, 2), tensor.WithBacking([]float32{5, 6, 7, 8}))

	nodeA := NodeFromAny(g, a, WithName("a"))
	nodeB := NodeFromAny(g, b, WithName("b"))

	nodeC, err := Add(nodeA, nodeB)
	if err != nil {
		log.Fatal(err)
	}

	machine := NewTapeMachine(g)
	if err := machine.RunAll(); err != nil {
		log.Fatal(err)
	}

	fmt.Printf("%v\n", nodeC.Value())
}
