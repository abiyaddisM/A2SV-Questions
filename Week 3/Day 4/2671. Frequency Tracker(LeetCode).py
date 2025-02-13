# February 13 2025
# https://leetcode.com/problems/frequency-tracker/
class FrequencyTracker:

    def __init__(self):
        self.freq = {}
        self.revfreq = {}

    def add(self, n: int) -> None:
        self.freq[n] = self.freq.get(n, 0) + 1
        f = self.freq[n]

        if self.freq[n] > 1:
            self.revfreq[f - 1] -= 1
        self.revfreq[f] = self.revfreq.get(f, 0) + 1

    def deleteOne(self, n: int) -> None:
        if n not in self.freq:
            return
        self.revfreq[self.freq[n]] -= 1
        self.freq[n] -= 1
        if self.freq[n] == 0:
            del self.freq[n]
        else:
            self.revfreq[self.freq[n]] = self.revfreq.get(self.freq[n], 0) + 1

    def hasFrequency(self, f: int) -> bool:
        if f not in self.revfreq or self.revfreq[f] == 0:
            return False
        return True

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
