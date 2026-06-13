# 27. Remove Element

## Intuition

My idea was to simply remove every occurrence of `val` from the list and keep the remaining elements.

## Approach

* Traverse the array using a list comprehension.
* Keep only the elements where `x != val`.
* Replace the original array using slice assignment (`nums[:] = ...`) so it is modified in-place.
* Return the length of the updated array.

## Key Idea

Filter out the unwanted value and overwrite the original list with the filtered result.

## Time Complexity

**O(n)**

(Traverse the array once.)

## Space Complexity

**O(n)**

(A new temporary list is created by the list comprehension.)

## Pattern

* Array
* List Comprehension
* Filtering

## Notes

This solution is simple and readable. However, it uses extra space by creating a new list instead of solving the problem with an in-place two-pointer approach.
