# February 10 2025
# https://leetcode.com/problems/4sum-ii/description/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        ldic = {}
        rdic = {}
        for i in range(len(nums1)):
            for j in range(len(nums1)):
                key1 = nums1[i] + nums2[j]
                key2 = nums3[i] + nums4[j]
                ldic[key1] = ldic.get(key1, 0) + 1
                rdic[key2] = rdic.get(key2, 0) + 1
        count = 0
        print(ldic, rdic)
        for key, val in ldic.items():
            if -key in rdic:
                count += (val * rdic[-key])
        return count
