class Solution(object):
    def shuffle(self, nums, n):
        """
        Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
        Return the array in the form [x1,y1,x2,y2,...,xn,yn].
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        nums_new = []
        nums_first = nums[:n]
        nums_last = nums[n:]
        for x in range(n):
            nums_new.append(nums_first[x])
            nums_new.append(nums_last[x])
        return nums_new
