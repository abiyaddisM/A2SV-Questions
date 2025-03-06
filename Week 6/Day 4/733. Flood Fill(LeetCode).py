# March 6 2025
# https://leetcode.com/problems/flood-fill/description/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if color == image[sr][sc]:
            return image
        cur = image[sr][sc]
        image[sr][sc] = color
        if 0 <= sr - 1 and image[sr - 1][sc] == cur:
            self.floodFill(image, sr - 1, sc, color)

        if len(image) > sr + 1 and image[sr + 1][sc] == cur:
            self.floodFill(image, sr + 1, sc, color)

        if 0 <= sc - 1 and image[sr][sc - 1] == cur:
            self.floodFill(image, sr, sc - 1, color)

        if len(image[sr]) > sc + 1 and image[sr][sc + 1] == cur:
            self.floodFill(image, sr, sc + 1, color)

        return image


