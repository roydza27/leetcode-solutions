# 3614. Process String with Special Operations II

# Intuition

The final string can be as large as 10^15 characters, so constructing it is impossible. Instead, track only the length after each operation and trace the target index k backwards.

# Approach

1. Compute the length after every operation.
2. If k is outside the final length, return ".".
3. Traverse the operations in reverse.
4. Map k back to its position before each operation.
5. When k corresponds to a newly added letter, return that letter.

# Time Complexity

O(n)

# Space Complexity

O(n)

# Pattern

Reverse Simulation
Index Mapping

# Notes

A straightforward brute-force simulation. Suitable when the final string size remains within limits.
