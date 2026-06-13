# 13. Roman to Integer

## Intuition
Convert the string by looking at characters one by one. If two characters together make a special case (like IV or CM), handle them as a pair.

## Approach
I mapped all Roman numerals, including special subtractive pairs like "IV", "XL", and "CM", into a dictionary. I use a while loop to traverse the string. At each step, I check if the next two characters form a known pair. If they do, I add that value and skip ahead two spots. Otherwise, I just add the single character's value and move one spot forward.

## Key Idea
Including the subtractive combinations (IV, IX, etc.) directly in the hash map to avoid complex subtraction logic.

## Time Complexity
O(n) - We iterate through the string once.

## Space Complexity
O(1) - The dictionary size is fixed regardless of input string length.

## Pattern
Hash Map, String Simulation

## Notes
Checking for double characters first prevents having to look back and subtract later.
