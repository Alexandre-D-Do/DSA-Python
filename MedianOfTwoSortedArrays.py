

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        size = len(nums1)
        if size % 2 != 0:
            median_index= (size / 2) - 0.5
            return nums1[int(median_index)]
        else:
            median_index1 = (size / 2)
            median_index2 = (median_index1 - 1)
            return (nums1[int(median_index1)] + nums1[int(median_index2)]) / 2