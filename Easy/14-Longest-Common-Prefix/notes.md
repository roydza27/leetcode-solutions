# 14. Longest Common Prefix

## Intuition
Assume the first string is the common prefix. Then, compare it with every other string and trim it down whenever there's a mismatch.

## Approach
I start by taking the first string in the list as my initial prefix. Then I loop through the rest of the strings. For each string, I keep removing the last character from my prefix until the current string starts with that prefix. If the prefix becomes an empty string at any point, it means there's no common prefix at all.

## Key Idea
Iteratively shortening the candidate prefix using `startswith()` and string slicing.

## Time Complexity
O(S) - Where S is the total number of characters across all strings in the input list.

## Space Complexity
O(1) - I'm only storing the prefix string, no additional complex data structures.

## Pattern
Horizontal Scanning, String Manipulation

## Notes
This approach is straightforward because it progressively narrows down the prefix by checking it against one string at a time.
