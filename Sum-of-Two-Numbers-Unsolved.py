class Solution:
    def solve(self, nums, k):
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j])== k and i != j:
                    return True;
                    break
        else:
            return False