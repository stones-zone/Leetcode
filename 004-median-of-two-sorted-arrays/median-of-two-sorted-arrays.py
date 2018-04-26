# -*- coding:utf-8 -*-


# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
#
#
# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5
#
#


#O(log(min(M,N)))
class Solution(object):
    def findMedianSortedArrays1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N1, N2 = len(nums1), len(nums2)
        if N1 < N2: 
            nums1, N1, nums2, N2 = nums2, N2, nums1, N1
        l, r = 0, N2*2
        while l <= r:
            j = (l + r) >> 1
            i = N1 + N2 - j
            L1 = -sys.maxint-1 if i == 0 else nums1[(i-1)>>1]
            L2 = -sys.maxint-1 if j == 0 else nums2[(j-1)>>1]
            R1 = sys.maxint if i == 2*N1 else nums1[i>>1]
            R2 = sys.maxint if j == 2*N2 else nums2[j>>1]
            if L1 > R2: l = j + 1
            elif L2 > R1: r = j - 1
            else:
                return (max(L1, L2) + min(R1, R2))/2.0
    
    def findMedianSortedArrays(self, nums1, nums2):        
        nums = nums1+nums2
        nums.sort()
        
        if len(nums)%2:
            return nums[len(nums)/2]
        else:
            return (nums[len(nums)/2-1]+nums[len(nums)/2])*0.5
