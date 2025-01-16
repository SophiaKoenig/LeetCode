class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        2769. Find the Maximum Achievable Number
        An integer x is called achievable if it can become equal to num
        after applying the following operation no more than t times:

        Increase or decrease x by 1, and simultaneously increase or decrease num by 1.
        Return the maximum possible achievable number.
        It can be proven that there exists at least one achievable number.
        :type num: int
        :type t: int
        :rtype: int
        """

        x = num
        t1 = t

        for number in range(t):
            x += 1
            t -= 1

        return x + t1
