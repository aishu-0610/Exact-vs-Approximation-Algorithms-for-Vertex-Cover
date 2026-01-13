# Exact-vs-Approximation-Algorithms-for-Vertex-Cover

Overview:
This project studies two algorithms for the Vertex Cover problem, a classical NP-hard problem in graph theory. The goal is to study the trade-off between optimality and algorithmic simplicity by contrasting an exact exponential-time solution with a simple greedy approximation.
The implementation is intentionally restricted to small graph instances to allow direct comparison between optimal and heuristic solutions.

Methodology:
The project includes two approaches:

1. Optimal Vertex Cover (Exact)
- Enumerates vertex subsets of increasing size
- Checks feasibility using exhaustive search
- Guarantees an optimal solution
- Time complexity is exponential, suitable only for small graphs
2. Greedy Vertex Cover (Approximation)
- Iteratively selects both endpoints of an uncovered edge
- Runs in polynomial time
- Produces a valid vertex cover with a known 2-approximation guarantee

Key Concepts Demonstrated:
- NP-hard optimisation problems
- Exact vs approximation algorithms
- Exhaustive subset enumeration
- Greedy heuristics and approximation ratios

Academic Context:
This project serves as preparatory work for engaging with graph theory, combinatorial optimisation, and approximation algorithms, particularly in understanding how heuristic methods trade optimality for efficiency. It serves as preparatory work for engaging with research on algorithmic guarantees and limitations.
