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
