# November 7 2025
# https://leetcode.com/problems/partition-labels/description/
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        par_dic = {}
        for i, ch in enumerate(s):
            if ch not in par_dic:
                par_dic[ch] = [i, i]
            else:
                par_dic[ch][1] = i

        intervals = sorted(par_dic.values(), key=lambda x: x[0])

        res = []
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if cur_start <= end:
                end = max(end, cur_end)
            else:
                res.append(end - start + 1)
                start, end = cur_start, cur_end

        res.append(end - start + 1)
        return res
