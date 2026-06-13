# 26. Remove Duplicates from Sorted Array

## Intuition
Because the array is already sorted, any duplicate numbers will be right next to each other. I just need to skip the ones that are the same as the previous number.

## Approach
I used two pointers. The pointer `i` moves through every element in the array starting from the second one. The pointer `j` keeps track of the position where the next unique element should be placed. If `nums[i]` is different from `nums[i-1]`, it's a new unique number, so I move it to `nums[j]` and increment `j`.

## Key Idea
In-place modification using a slow and fast pointer approach.

## Time Complexity
O(n) - A single pass through the array.

## Space Complexity
O(1) - No extra space used; the array is modified in-place.

## Pattern
Two Pointers

## Notes
The value of `j` at the end represents the number of unique elements found.
