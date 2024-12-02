class Solution(object):
    def interpret(self, command):
        """
        You own a Goal Parser that can interpret a string command.
        The command consists of an alphabet of "G", "()" and/or "(al)" in some order.
        The Goal Parser will interpret "G" as the string
        "G", "()" as the string "o", and "(al)" as the string "al".
        The interpreted strings are then concatenated in the original order.
        Given the string command, return the Goal Parser's interpretation of command.
        :type command: str
        :rtype: str
        """
        '''result = ""
        i = 0
        while i < len(command):
            if i == "G":
                result += "G"
                i += 1
            elif command[i:i+2] == "()":
                result += "o"
                i += 2
            elif command[i:i+4] == "(al)":
                result += "al"
                i += 4
        return result'''
        return command.replace("()", "o").replace("(al)", "al")
