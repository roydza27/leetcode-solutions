# 35. Search Insert Position

## Intuition

Use binary search to find the target. If it doesn't exist, the position where the search ends is the correct insertion index.

## Approach

* Initialize `left` and `right`.
* Find the middle element.
* If `nums[mid] == target`, return `mid`.
* If the target is smaller, search the left half.
* Otherwise, search the right half.
* When the loop ends, return `left` as the insertion position.

## Key Idea

Binary search narrows the search space, and `left` naturally points to where the target should be inserted if it's not found.

## Time Complexity

**O(log n)**

## Space Complexity

**O(1)**

## Pattern

* Binary Search
* Sorted Array

## Notes

Efficient solution that handles both finding the target and determining its insertion position using the same binary search logic.
