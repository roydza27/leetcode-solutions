# 4. Median of Two Sorted Arrays

## Difficulty

Hard

## Intuition

Combine both arrays into one, sort it, and find the median based on whether the total number of elements is odd or even.

## Approach

- Create a new list.
- Add all elements from `nums1` and `nums2`.
- Sort the merged list.
- If the length is odd, return the middle element.
- If the length is even, return the average of the two middle elements.

## Key Idea

The median depends only on the sorted order of all elements, so merge and sort first, then compute the middle value(s).

## Time Complexity

- **O((m+n) log(m+n))**

## Space Complexity

- **O(m+n)**

## Pattern

- Array
- Sorting

## Notes

- Remember to sort after merging.
- For even length, use:
  ```python
  (arr[n//2 - 1] + arr[n//2]) / 2.0
  ```
- Use `/` instead of `//` to avoid floor division.
- Be careful to use `list1`, not the built-in `list`.
