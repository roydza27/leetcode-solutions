# 6. Zigzag Conversion

## Intuition

At first, I tried finding an index pattern and even removing characters after processing them. But it became confusing because the jumps between indices change for different rows. Then I realized it's easier to simulate the zigzag movement.

## Approach

* If `numRows == 1`, return the string.
* Create an array for each row.
* Keep track of the current row and the direction (down/up).
* Place each character in the current row.
* Change direction when reaching the top or bottom.
* Finally, join all the rows to get the answer.

## Key Idea

Instead of calculating the final indices, simulate the row movement:

* For 3 rows: `0 → 1 → 2 → 1 → 0 ...`
* For 4 rows: `0 → 1 → 2 → 3 → 2 → 1 → 0 ...`

## Time Complexity

**O(n)**

## Space Complexity

**O(n)**

## Pattern

* Simulation
* String Manipulation

## Notes

I initially spent time trying to derive a mathematical pattern for the indices using variables like `mul`, but eventually understood that simply simulating the zigzag traversal with a `currentRow` and direction variable makes the solution much simpler.
