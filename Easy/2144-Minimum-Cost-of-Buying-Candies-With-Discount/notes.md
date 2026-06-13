# 2144. Minimum Cost of Buying Candies With Discount

## Intuition
To get the best discount, I should always try to get the most expensive candy for free after buying two even more expensive ones.

## Approach
I sorted the costs in descending order so the most expensive candies are at the front. Then, I used a while loop to take candies in groups of three. I "buy" the first two (add them to the total) and "pop" the third one as the free one. After the loop, if there are any candies left (less than 3), I just add their costs to the total since I can't get a discount on them.

## Key Idea
Sorting the array in reverse to greedily pick the highest values for the "free" slots.

## Time Complexity
O(n²) - Sorting takes O(n log n), but using `pop(0)` inside the loop is O(n) for each removal, leading to O(n²) overall.

## Space Complexity
O(1) - The sorting is done in-place and I only use a few variables for counting.

## Pattern
Greedy, Sorting

## Notes
Using `pop(0)` makes the solution a bit slower than it could be if I used an index pointer or sliced the array, but it gets the job done for this problem.
