class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        s2 = ''.join(e for e in s if e.isalnum())
        s1 = s2.lower()
        n = 0
        length = len(s1)
        left = 0
        right = len(s1) - 1

        while left <= right:
            if s1[left] != s1[right]:
                return False
            left += 1
            right -= 1
        return True