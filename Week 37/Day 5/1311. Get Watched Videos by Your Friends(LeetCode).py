# October 10 2025
# https://leetcode.com/problems/get-watched-videos-by-your-friends/description/
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> \
    List[str]:
        n = len(friends)
        visited = [False] * n

        visited[id] = True
        q = deque([id])
        curr = 0

        while q and curr < level:
            for _ in range(len(q)):
                person = q.popleft()
                for f in friends[person]:
                    if not visited[f]:
                        visited[f] = True
                        q.append(f)

            curr += 1

        video = Counter()
        for f in q:
            video.update(watchedVideos[f])
        ans = sorted(video.keys(), key=lambda x: (video[x], x))
        return ans




