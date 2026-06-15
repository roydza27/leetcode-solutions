class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1

        maxx=0

        while left<right:
            gap = right-left
            minHeight = min(height[left], height[right])
            maxxSum = minHeight * gap
            maxx= max(maxxSum, maxx)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxx