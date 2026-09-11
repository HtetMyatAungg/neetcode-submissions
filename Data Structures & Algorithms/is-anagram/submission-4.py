class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h_s = {}
        h_t = {}

        for l in s:
            h_s[l] = 0
        for l in s:
            h_s[l] += 1
        for l in t:
            h_t[l] = 0
        for l in t:
            h_t[l] += 1
        return h_s == h_t