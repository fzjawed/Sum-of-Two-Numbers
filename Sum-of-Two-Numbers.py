class Solution:
    def solve(self, nums, k):
        s = set()
        for e in nums:
            if k - e in s:
                return True
            s.add(e)
        return False