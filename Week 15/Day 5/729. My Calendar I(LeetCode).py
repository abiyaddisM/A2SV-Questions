# May 9 2025
# https://leetcode.com/problems/my-calendar-i/description/
class MyCalendar:

    def __init__(self):
        self.date = []

    def book(self, st: int, ed: int) -> bool:
        temp = self.date
        if not temp:
            temp.append([st, ed])
            return True
        l = 0
        r = len(temp) - 1
        while l <= r:
            m = (r + l) // 2
            if temp[m][0] == st:
                return False
            elif temp[m][0] > st:
                r = m - 1
            else:
                l = m + 1
        if r >= 0:
            if st < temp[r][1]:
                return False
        if l < len(temp):
            if temp[l][0] < ed:
                return False
        temp.insert(l, [st, ed])
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)