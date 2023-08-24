**Importing Libraries :**

- 'fmt': The standard Go library for formatting and producing outputs.
- 'log': The standard Go library for logging errors.
- ."gorgonia.org/gorgonia": Imports the Gorgonia library with a "." alias, allowing functions to be called without a prefix.
- gorgonia.org/tensor: Imports the tensor manipulation library from Gorgonia.

**Main Function('main')**
1. **Creating a Computational Graph:** <br>
- g := NewGraph(): Creates a new graph. In the Gorgonia context,
a graph is where all the computations are defined.
2. **Tensor Creation:**
- **a** and **b** are 2x2 tensors instantiated with specific values. Tensors are multi-dimensional arrays,
and in this case, they are matrices.
3. **Adding Tensors to the Graph:**
- nodeA := NodeFromAny(g, a, WithName("a")): Creates a node inside the graph g representing the
tensor a and names it "a".
- nodeB := NodeFromAny(g, b, WithName("b")): Similar to the previous one but for tensor b.
4. **Addition Operation:**
- nodeC, err := Add(nodeA, nodeB): Adds the nodeA and nodeB together. The result is stored in nodeC.
5. **Evaluating the Graph:**
- machine := NewTapeMachine(g): Instantiates a new machine to evaluate the graph. This machine will evaluate all
operations in the sequence they're defined in the graph.
- if err := machine.RunAll(); err != nil: Executes all the operations in the graph.
If there's an error during execution, the error will be logged.
**Displaying the Output:**
- fmt.Printf("%v\n", nodeC.Value()): Prints the value of nodeC to the console,
showing the result of the tensor addition.

**Purpose of the Project:**
<p>
The main objective of this project is to demonstrate the basic capabilities of the Gorgonia library 
  in performing mathematical operations on tensors, specifically addition in this case. 
  It aims to introduce the user to the process of defining, computing, 
  and evaluating operations in a computational graph. The code, while simple, 
  lays the groundwork for more complex machine learning 
  or numerical analysis tasks that Gorgonia is capable of handling.
</p>

Example :
```
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

```
