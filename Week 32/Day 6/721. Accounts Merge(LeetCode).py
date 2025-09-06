# September 6 2025
# https://leetcode.com/problems/accounts-merge/description/
class Solution:
    def accountsMerge(self, acc: List[List[str]]) -> List[List[str]]:
        parent = [i for i in range(len(acc))]
        def find(x):
            if x == parent[x]:
                return x
            temp = find(parent[x])
            parent[x] = temp
            return temp
        def union(a, b):
            t1 = find(a)
            t2 = find(b)
            if t1 != t2:
                parent[t2] = t1

        for i in range(len(acc)):
            for j in range(i + 1, len(acc)):
                if acc[i][0] != acc[j][0]:
                    continue
                for k in range(1,len(acc[i])):
                    if acc[i][k] in acc[j]:
                        union(i, j)
                        break
        dic = defaultdict(set)
        for i in range(len(parent)):
            t = find(parent[i])
            dic[t].update(acc[i][1:])
        res = []
        for k, v in dic.items():
            temp = [acc[k][0]]
            l = list(v)
            l.sort()
            temp.extend(l)
            res.append(temp)
        return res
