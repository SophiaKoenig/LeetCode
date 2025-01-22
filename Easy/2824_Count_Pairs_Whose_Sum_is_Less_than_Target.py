class Solution(object):
    def countPairs(self, nums, target):
        """
        Given a 0-indexed integer array nums of length n and an integer target,
        return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

        :type nums: List[int]
        :type target: int
        :rtype: int

        """
        output = 0

        for i, v in enumerate(nums):
            for j, w in enumerate(nums):
                if i < j and (v + w) < target:
                   output += 1

        return output

