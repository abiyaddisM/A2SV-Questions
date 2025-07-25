# July 25 2025
# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
class Solution:
    def sortItems(self, n: int, m: int, g: List[int], bi: List[List[int]]) -> List[int]:
        group = [[] for i in range(m)]
        for i in range(n):
            if g[i] == -1:
                g[i] = len(group)
                group.append([i])
                continue
            group[g[i]].append(i)
        innerDic = {}
        for i in range(len(group)):
            for j in range(len(group[i])):
                innerDic[group[i][j]] = j
        outerGraph = [[] for i in range(len(group))]
        outerDegree = [0 for i in range(len(group))]

        innerGraph = [[[] for _ in range(len(group[i]))] for i in range(len(group))]
        innerDegree = [[0 for _ in range(len(group[i]))] for i in range(len(group))]
        for i in range(len(bi)):
            for j in range(len(bi[i])):
                if g[bi[i][j]] == g[i]:
                    innerGraph[g[i]][innerDic[bi[i][j]]].append(innerDic[i])
                    innerDegree[g[i]][innerDic[i]] += 1
                    continue
                outerGraph[g[bi[i][j]]].append(g[i])
                outerDegree[g[i]] += 1
        innerRes = []
        for i in range(len(innerGraph)):
            que = deque()
            temp = []
            for j in range(len(innerDegree[i])):
                if not innerDegree[i][j]:
                    que.append(j)
            while que:
                j = que.popleft()
                temp.append(group[i][j])
                for k in innerGraph[i][j]:
                    innerDegree[i][k] -= 1
                    if not innerDegree[i][k]:
                        que.append(k)
            if len(temp) != len(group[i]):
                return []
            innerRes.append(temp)
        que = deque()
        for i in range(len(outerDegree)):
            if not outerDegree[i]:
                que.append(i)
        outerRes = []
        while que:
            node = que.popleft()
            outerRes.append(innerRes[node])
            for i in outerGraph[node]:
                outerDegree[i] -= 1
                if not outerDegree[i]:
                    que.append(i)
        res = []
        for i in range(len(outerRes)):
            res.extend(outerRes[i])
        if len(res) != n:
            return []
        return res
