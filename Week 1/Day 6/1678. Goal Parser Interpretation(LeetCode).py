#Febuary 1 2025
#https://leetcode.com/problems/goal-parser-interpretation/description/
class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                res += "G"
                i += 1
            elif command[i + 1] == "a":
                res += "al"
                i += 4
            else:
                res += "o"
                i += 2
        return res
