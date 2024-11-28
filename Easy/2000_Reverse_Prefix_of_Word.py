class Solution(object):
    def reversePrefix(self, word : str, ch : str):
        """
        Given a 0-indexed string word and a character ch,
        reverse the segment of word that starts at index 0 and ends
        at the index of the first occurrence of ch (inclusive).
         If the character ch does not exist in word, do nothing.

        For example, if word = "abcdefd" and ch = "d",
        then you should reverse the segment that starts at 0 and ends at 3 (inclusive).
        The resulting string will be "dcbaefd".
        Return the resulting string.
        :type word: str
        :type ch: str
        :rtype: str
        """
        part1 = ""
        part2 = ""

        for character in range(len(word)):
            if ch == word[character]:
                part1 = word[0:character + 1:]
                part1 = part1[::-1]
                part2 = word[character + 1:]

                return part1 + part2

        return word