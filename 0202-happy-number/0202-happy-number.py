class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(c)**2 for c in str(n))
            if n == 1: return True
        return False
