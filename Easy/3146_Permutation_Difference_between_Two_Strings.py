class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        You are given two strings s and t such that every character occurs at most once in s and t is a permutation of s.
        The permutation difference between s and t is defined
        as the sum of the absolute difference between the index of the
        occurrence of each character in s and the index of the occurrence of the same character in t.

        Return the permutation difference between s and t.

        :type s: str
        :type t: str
        :rtype: int
        """
        counter = 0

        for i in range(len(s)):
            if s[i] != t[i]:
                index1 = i
                for j in range(len(t)):
                    if s[index1] == t[j]:
                        counter += abs(index1 - j)

        return counter
