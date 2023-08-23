MathNet.Numerics is a mathematical library for .NET, offering a plethora of numerical methods for solving mathematical problems. In this example, we demonstrate how to use MathNet.Numerics to:

Create matrices and vectors.
Perform basic operations on matrices and vectors.
Solve a system of linear equations.
To start, we need to install the package:

```
Install-Package MathNet.Numerics
```

Sample code with explanations:

```
using System;
using MathNet.Numerics.LinearAlgebra;

namespace MathNetExample
{
    class Program
    {
        static void Main(string[] args)
        {
            // 1. Create matrices and vectors
            var matrixA = Matrix<double>.Build.DenseOfArray(new double[,]
            {
                { 2, 1, 1 },
                { 1, 3, 2 },
                { 1, 0, 0 }
            });

            var vectorB = Vector<double>.Build.Dense(new double[] { 4, 5, 6 });

            Console.WriteLine("Matrix A:");
            Console.WriteLine(matrixA);
            Console.WriteLine("Vector B:");
            Console.WriteLine(vectorB);

            // 2. Basic operations on matrices and vectors
            var matrixC = matrixA.Transpose(); // Transpose matrix A
            Console.WriteLine("Transpose of Matrix A:");
            Console.WriteLine(matrixC);

            var resultVector = matrixA.Multiply(vectorB); // Result of matrix multiplied by vector
            Console.WriteLine("Result of multiplying Matrix A with Vector B:");
            Console.WriteLine(resultVector);

            // 3. Solve a system of linear equations Ax = B
            var solver = matrixA.QR().Solve(vectorB);
            Console.WriteLine("Solution of the system Ax = B:");
            Console.WriteLine(solver);
        }
    }
}
```
Explanation:

1. Creating matrices and vectors:
* Matrix<double>.Build.DenseOfArray(...) is used to create a matrix from a two-dimensional array.
* Vector<double>.Build.Dense(...) is used to create a vector from a one-dimensional array.

2. Basic operations on matrices and vectors:
* Transpose() is a method to get the transpose of a matrix.
* Multiply(vectorB) is a method to multiply the matrix with a vector.

3. Solving a system of linear equations Ax = B:
* QR() is the QR decomposition of the matrix, which is a technique for solving linear systems.
* Solve(vectorB) returns the solution vector x for the equation Ax = B.

  You can run the above code in a .NET environment with the MathNet.Numerics library already installed. <br>
  But i use visual studio code and for the install package you can do

```
dotnet add package MathNet.Numerics // add this to your file that have .csproj
```

## The result : <br>
![matrixmathnet](https://github.com/rifqanzalbina/DifferentButSame/assets/124742008/f2e0a336-82cc-41c2-9835-b5bcf83114cb)
