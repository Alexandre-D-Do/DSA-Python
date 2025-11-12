

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
        if size % 2 != 0:
            medianindex= (size / 2) - 0.5
            return nums1[int(medianindex)]
        else:
            medianindex1 = (size / 2)
            medianindex2 = (medianindex1 - 1)
            return (nums1[int(medianindex1)] + nums1[int(medianindex2)]) / 2