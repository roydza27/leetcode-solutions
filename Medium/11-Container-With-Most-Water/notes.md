# 11. Container With Most Water

## Intuition

I first thought of checking all pairs, but that would be too slow. Using two pointers from both ends helps find the maximum area efficiently.

## Approach

* Start with two pointers at the left and right ends.
* Calculate the area using the smaller height and the distance between them.
* Update the maximum area.
* Move the pointer with the smaller height inward.
* Repeat until the pointers meet.

## Key Idea

Always move the shorter line because moving the taller one cannot increase the area while the width decreases.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Pattern

* Two Pointers
* Greedy

## Notes

Initially, I considered sorting and checking different combinations, but sorting loses the original positions. The two-pointer approach solves the problem in a single pass.
