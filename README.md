# LeetCode 317 - Shortest Distance from All Buildings

## Problem Statement

You are given a grid containing buildings, empty land, and obstacles.

Find the empty land cell that has the shortest total Manhattan distance to all buildings.

Return the shortest distance. If there is no empty land cell that can reach every building, return `-1`.

## Example 1

### Input

```text
grid = [
  [1,0,2,0,1],
  [0,0,0,0,0],
  [0,0,1,0,0]
]
```

### Output

```text
7
```

## Example 2

### Input

```text
grid = [
  [1,0],
  [0,1]
]
```

### Output

```text
2
```

## Approach

Use **Breadth-First Search (BFS)** from every building.

For each building, calculate the shortest distance to every reachable empty cell. Store both the total distance and the number of buildings that can reach each empty cell.

Finally, choose the empty cell that can be reached by all buildings and has the minimum total distance.

## Algorithm

1. Create arrays to store total distances and building reach counts.
2. Traverse the grid to find every building.
3. Run BFS starting from each building.
4. For every reachable empty cell, update its total distance.
5. Increase its building reach count.
6. After processing all buildings, check every empty cell.
7. Consider only cells reachable from all buildings.
8. Return the minimum total distance.
9. Return `-1` if no valid cell exists.

## Time Complexity

`O((m × n)²)`

## Space Complexity

`O(m × n)`

## Key Concepts

* Breadth-First Search
* Grid
* Queue
* Shortest Path
* Matrix
* Distance Tracking

## Language

Python

## LeetCode Details

* **Problem:** 317
* **Title:** Shortest Distance from All Buildings
* **Difficulty:** Hard

## Author

**T. Nandhini Reddy**

GitHub: `242t605119-dotcom`
