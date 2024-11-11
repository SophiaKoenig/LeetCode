class Solution(object):
    def defangIPaddr(self, address: str):
        """
        Given a valid (IPv4) IP address, return a defanged version of that IP address.
        A defanged IP address replaces every period "." with "[.]".
        :type address: str
        :rtype: str
        """
        result = address
        address1 = address

        for i in range(len(address)):
            if address[i] == ".":
                part1 = address1[:i]
                part2 = address[i + 1:]
                result = part1 + "[.]" + part2
                address1 = result + part2
        return result

    def test(self, address):

        leng = len(address)
        result = address

        for i in range(leng):
            if address[i] == ".":
                part1 = result[:i]
                part2 = address[i + 1:]
                result = result[:i+1] + "[.]"
                i += 1
                leng += 1

    def test2(self, address):
        result = ""
        for i in address:
            if i == ".":
                result += "[.]"
            else:
                result += i

