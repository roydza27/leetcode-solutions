class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        list1 = []

        list1.extend(nums1)
        list1.extend(nums2)

        list1.sort()
        
        n = len(list1)

        if(n%2 == 1):
            return float(list1[n//2])
        else:
            return float((list1[n//2-1] + list1[n//2]) / 2.0)
        
