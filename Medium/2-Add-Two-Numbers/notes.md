# 2. Add Two Numbers

## Intuition
This is basically long addition from school. I just need to add the numbers digit by digit and keep track of the carry.

## Approach
I initialized a dummy head node to build the result list easily. I use a `while` loop that keeps going as long as there's a node left in either list or there's a leftover carry. For each step, I add the values from both nodes (if they exist) plus the carry. I store the remainder in a new node and update the carry for the next step.

## Key Idea
Using a dummy node to avoid handling the head separately and a `carry` variable to manage sums greater than 9.

## Time Complexity
O(max(N, M)) - Where N and M are the lengths of the two input linked lists.

## Space Complexity
O(max(N, M)) - I'm creating a new linked list to store the sum.

## Pattern
Linked List, Math

## Notes
The `while l1 or l2 or carry` condition is handy because it handles cases where the last addition generates a new carry at the end.
