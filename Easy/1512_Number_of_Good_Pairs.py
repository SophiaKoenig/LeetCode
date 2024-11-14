class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        Given an array of integers nums, return the number of good pairs.
        A pair (i, j) is called good if nums[i] == nums[j] and i < j.

        :type nums: List[int]
        :rtype: int
        """
        counter = 0

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i < j and nums[i] == nums[j]:
                    counter += 1

        return counter


sol = Solution()
nums = [1, 2, 3, 1, 1, 3]
sol.numIdenticalPairs(nums)
