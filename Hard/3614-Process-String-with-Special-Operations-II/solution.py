class Solution:
    def processStr(self, s: str, k: int) -> str:

        length = 0
        lengths = []

        for ch in s:
            if ch.isalpha():
                length += 1
            elif ch == "#":
                length *= 2
            elif ch == "%":
                pass
            elif ch == "*":
                length = max(0, length - 1)

            lengths.append(length)
        
        if k >= lengths[-1]:
            return "."

        for i in range(len(s) - 1, -1, -1):
            L = lengths[i-1] if i > 0 else 0

            ch = s[i]

            if ch.isalpha():
                if k == L:
                    return ch
            elif ch == '#':
                if k >= L:
                    k -= L
            elif ch == '%':
                k = L - 1 - k
            elif ch == '*':
                pass

        return "."

