# 175. Combine Two Tables

## Intuition
I need to get name and address info for everyone in the Person table. Since some people might not have an address, I can't use a regular join or they'd be filtered out.

## Approach
I used a `LEFT JOIN` to combine the `Person` table with the `Address` table using `PersonId` as the link. This way, all rows from the `Person` table stay in the result, and if there's no matching `PersonId` in the `Address` table, the City and State will just show up as NULL.

## Key Idea
Using `LEFT JOIN` to preserve all records from the primary table regardless of matches in the secondary table.

## Time Complexity
O(N + M) - Where N and M are the number of rows in the Person and Address tables respectively.

## Space Complexity
O(N + M) - Space needed to store and return the joined result set.

## Pattern
SQL LEFT JOIN

## Notes
A simple INNER JOIN would fail because it would skip people without an address.
