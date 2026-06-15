class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        left, right = 0, 0
        maxx = 0
        newstr = ""

        for i in range(len(s)):
            newstr = s[left:right]
            print(i,newstr)

            if s[i] in newstr:
                left += 1
            else:
                right += 1
                if len(s[left:right]) > maxx:
                    maxx = len(s[left:right])
                    print("Within ",maxx, right, left,s[left:right])
                    

        return maxx
