# 3. Longest Substring Without Repeating Characters

## Difficulty

Medium

## Intuition

Maintain a window containing only unique characters. If a duplicate appears, shrink the window from the left instead of restarting.

## Approach

- Keep two pointers: `left` and `right`.
- Expand the window by moving `right`.
- If a duplicate is found, move `left` until the window becomes valid.
- Update the maximum window length.

## Key Idea

Never restart the search. Continuously adjust the current window to maintain unique characters.

## Time Complexity

- **O(n)**

## Space Complexity

- **O(n)**

## Pattern

- Sliding Window
- Two Pointers

## Notes

- `right` expands the window.
- `left` shrinks the window when duplicates exist.
- A `while` loop is needed because moving `left` once may not remove the duplicate.
- Keep updating the maximum valid window length.
