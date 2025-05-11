# May 11 2025
# https://leetcode.com/problems/intersection-of-two-arrays-ii/
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = Counter(nums1)
        dic2 = Counter(nums2)
        res = []
        for k, v in dic1.items():
            if k in dic2:
                for _ in range(min(v, dic2[k])):
                    res.append(k)
        return res

