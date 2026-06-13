# 1. Two Sum

## Intuition
Brute force approach. I just need to check every possible pair of numbers to see if they add up to the target.

## Approach
First, I copy the input array into a new one. Then I use nested loops where the outer loop goes through each element and the inner loop checks all previous elements to see if their sum matches the target.

## Key Idea
Checking all pairs using two pointers/nested loops.

## Time Complexity
O(n²) - Two nested loops iterate through the array.

## Space Complexity
O(n) - A copy of the input array is created.

## Pattern
Brute Force, Array

## Notes
The array copy isn't strictly necessary but it's how I handled it. A hash map would be faster, but this works for smaller inputs.
