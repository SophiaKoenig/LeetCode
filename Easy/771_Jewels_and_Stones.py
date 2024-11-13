class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        You're given strings jewels representing the types of stones that are jewels,
         and stones representing the stones you have.
         Each character in stones is a type of stone you have.
          You want to know how many of the stones you have are also jewels.
        Letters are case sensitive, so "a" is considered a different type of stone from "A".
        """
        dic = {}
        counter = 0

        for char in jewels:
            dic[char] = char

        for i in stones:
            if i in dic:
                counter += 1
        return counter


class Solution2(object):
    def numJewelsInStones(self, J, S):
        return sum(S.count(j) for j in J)
