# June 8 2025
# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        len1 = len(nums1)
        len2 = len(nums2)

        total_half = (len1 + len2 + 1) // 2

        l = 0
        r = len1

        while l <= r:
            m1 = l + (r - l) // 2
            m2 = total_half - m1

            i1 = float('-inf') if m1 == 0 else nums1[m1 - 1]
            i2 = float('inf') if m1 == len1 else nums1[m1]

            j1 = float('-inf') if m2 == 0 else nums2[m2 - 1]
            j2 = float('inf') if m2 == len2 else nums2[m2]

            if i1 > j2:
                r = m1 - 1
            elif j1 > i2:
                l = m1 + 1
            else:

                if (len1 + len2) % 2 != 0:
                    return float(max(i1, j1))
                else:
                    return float(max(i1, j1) + min(i2, j2)) / 2.0
