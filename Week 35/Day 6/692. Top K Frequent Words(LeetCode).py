# September 27 2025
# https://leetcode.com/problems/top-k-frequent-words/description/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dic = Counter(words)
        temp = []
        for word, freq in dic.items():
            temp.append([freq, word])

        temp.sort(key=lambda x: (-x[0], x[1]))

        return [word for freq, word in temp[:k]]
