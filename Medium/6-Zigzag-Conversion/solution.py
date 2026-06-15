class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1:
            return s

        rows = [""] * numRows

        print(len(rows))

        currentRow = 0
        goingDown = True

        for ch in s:
            rows[currentRow] += ch
            if currentRow == 0:
                goingDown = True
            if currentRow == numRows-1:
                goingDown = False
            if goingDown:
                currentRow+=1
            else:
                currentRow-=1

        return "".join(rows)

            




