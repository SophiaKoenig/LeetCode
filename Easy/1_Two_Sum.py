class Solution(object):
    def twoSum(self, nums, target):
        """
        Given an array of integers nums and an integer target,
         return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution,
         and you may not use the same element twice.
        You can return the answer in any order.
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}

        for index, value in enumerate(nums):
            searching = target - value
            if searching in dic:
                return [dic[searching], index]
            else:
                dic[value] = index
