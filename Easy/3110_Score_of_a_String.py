class Solution(object):
    def scoreOfString(self, s):
        """
        You are given a string s.
        The score of a string is defined as the sum of the absolute difference between
        the ASCII values of adjacent characters.
        Return the score of s.

        :type s: str
        :rtype: int
        """
        sum = 0

        for number in range(len(s) - 1):
            current = abs(ord(s[number]))
            next = abs(ord(s[number + 1]))
            sum += abs(current - next)


        return sum