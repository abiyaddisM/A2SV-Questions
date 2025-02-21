# February 21 2025
# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        for i in range(len(image)):
            for j in range(len(image[i]) // 2 + (1 if len(image[i]) % 2 == 1 else 0)):
                image[i][j], image[i][-(j + 1)] = image[i][-(j + 1)], image[i][j]
                image[i][j] = 1 if image[i][j] == 0 else 0
                if len(image[i]) - j != j + 1:
                    image[i][-(j + 1)] = 1 if image[i][-(j + 1)] == 0 else 0

        return image 