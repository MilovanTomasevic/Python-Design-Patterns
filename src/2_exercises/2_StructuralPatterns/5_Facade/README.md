## Facade Coding Exercise
A `magic square` is a square matrix of numbers where the sum in each row, each column, and each of the diagonals is the same.

You are given a system of 3 classes that can be used to make a magic square. The classes are:

- *Generator*: this class generates a 1-dimensional list of random digits in range 1 to 9.
- *Splitter*: this class takes a 2D list and splits it into all possible arrangements of 1D lists. It gives you the columns, the rows and the two diagonals.
- *Verifier*: this class takes a 2D list and verifies that the sum of elements in every sublist is the same.

Please implement a Façade class called `MagicSquareGenerator`  which simply generates the magic square of a given size.