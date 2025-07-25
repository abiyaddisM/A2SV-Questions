# July 25 2025
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/
class Solution:
    def findAllRecipes(self, recipes: List[str], ing: List[List[str]], supplies: List[str]) -> List[str]:
        dic = {}
        for i in range(len(recipes)):
            dic[recipes[i]] = i
        sup = set(supplies)
        graph = [[] for _ in range(len(recipes))]
        degree = [len(ing[i]) for i in range(len(recipes))]
        res = []
        for i in range(len(recipes)):
            for j in range(len(ing[i])):
                if ing[i][j] in sup:
                    degree[i] -= 1
                if ing[i][j] not in sup and ing[i][j] in dic:
                    graph[dic[ing[i][j]]].append(i)

        que = deque()
        for i in range(len(degree)):
            if not degree[i]:
                que.append(i)
        while que:
            node = que.popleft()
            res.append(recipes[node])
            for i in graph[node]:
                degree[i] -= 1
                if not degree[i]:
                    que.append(i)

        return res