# 28. Find the Index of the First Occurrence in a String

## Intuition

Check if `needle` exists in `haystack`. If it does, return its first index; otherwise return `-1`.

## Approach

* Use `in` to check whether `needle` is present.
* If found, use `find()` to get its first occurrence.
* If not found, return `-1`.

## Key Idea

Use Python's built-in string operations instead of manually traversing the string.

## Time Complexity

**O(n)**

## Space Complexity

**O(1)**

## Pattern

* String
* Built-in Functions

## Notes

Simple and readable solution that relies on Python's built-in methods.
