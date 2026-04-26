class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {} # letter -> count
        mapT = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        for k in mapS:
            if mapS[k] != mapT.get(k, 0):
                return False
        return True