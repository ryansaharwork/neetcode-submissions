class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = sorted(s)
        stringT = sorted(t)

        return stringS == stringT