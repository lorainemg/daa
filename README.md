# DAA Problems
This repository contains solutions for several problems given in the DAA subject.

## Problem 1

This problem seeks to minimize the total cost of a set of objects that increases as time progresses, where the increase of the latter is not constant, but depends on the distances. between those objects. First, a brute force approach is tested to analyze the characteristics of the problem, obtaining all the possible solutions and returning from these the one with the lowest cost, having a complexity of O(n ∗ n!). After realizing several interesting properties of the problem, an optimization of the previous algorithm is developed, generating fewer permutations to analyze. Then, a recursive solution is carried out in which all possible cases are explored, taking 2 possible decisions with a cost of O(n ∗ 2n). Finally, in order to reduce the complexity of the algorithms, several greedy solutions are developed that seek to minimize the cost of the objects. After several attempts, it is concluded that this approach may not be the right one for resolution.

The full report were all the solutions of this problem are analyzed can be found in [Problema1.pdf](https://github.com/lorainemg/daa/blob/main/Problem%201/Report/Problema1.pdf).

## Problem 2

This problem consists of, given a list of `l` numbers, determining the number of ways to equalize all the numbers to a value `h` by adding only 1 to intervals of numbers, with the restriction that the same interval cannot be selected twice. After proving several properties that these lists must meet in order to obtain a valid result, a brute force algorithm is developed that consists of generating all the possible intervals that make up a given set and then those to which transformations will be applied will be selected, subsequently checking if they are solutions with a cost of at most $O(n^2 ∗ 2^{n^2})$. Several dynamic ways of solving the problem were then tried, the final dynamic turned out to be too costly to consider. Finally, an algorithm is developed that, despite being unsuccessful, it is believed that a similar approach could solve the problem.

The full report for this problem can be found at [Problema2.pdf](https://github.com/lorainemg/daa/blob/main/Problem%202/Report/Problema2.pdf).

## Problem 3

This problem consists of matching one list with another in the least number of steps, taking into account that there is a number `n` that will represent the maximum element of both lists at all times. First, we carry out a simplification of the problem that, although it is not a solution, constitutes a good approximation. It is assumed that the behavior is towards a single direction and the minimum number of steps is returned to match both lists through a dynamic solution with a cost of $O(n^2)$. Then, it decides to be much less efficient but more correct with a brute force solution that iterates over the first `c` numbers, where `c` is the minimum number of moves expected. After this, a recursive solution is developed that has a divide-and-conquer approach, seeking to obtain the optimal response by dividing the list into intervals and returning from these the minimum number of moves to equal them to a certain value with a cost of $O(n^ 2 * |l^3|)$. Finally, it is a bit more efficient to transform the recursive definition into a dynamic one.

The report of this problem ca be found at [Problema3.pdf](https://github.com/lorainemg/daa/blob/main/Problem%203/Report/Problema3.pdf).

## Problem 4

This problem's objective is to find the partition defined on a set `A` that has a minimum cost, which in turn depends on the costs of the subsets contained in it. For the calculation of the cost of the subsets, their cardinality and their position in the partition become important. First, a brute force algorithm is performed that generates all the possible partitions, then all the orderings that the subgroups will have are calculated and the one with the lowest cost is chosen, obtaining a cost of $O(B_n ∗ n! ∗ n)$ . Next, this algorithm is improved by determining the best ordering for the subsets, improving the cost to $O(Bn ∗ n^2)$. Finally, a dynamic solution is tried that, despite being unsuccessful, serves as a preliminary for another whose cost will be $O(n^3)$.

The report of this problem is in [Problema4.pdf](https://github.com/lorainemg/daa/blob/main/Problem%204/Report/Problema4.pdf).