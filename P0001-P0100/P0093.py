from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        if n == 0 or n > 12:
            return []

        addresses = []
        for s1 in range(1, n - 1):
            d1 = s[:s1]
            if not self._check(d1):
                continue
            for s2 in range(s1 + 1, n - 1):
                d2 = s[s1:s2]
                if not self._check(d2):
                    continue
                for s3 in range(s2 + 1, n):
                    d3 = s[s2:s3]
                    d4 = s[s3:]
                    if not self._check(d3) or not self._check(d4):
                        continue
                    address = ".".join([d1, d2, d3, d4])
                    addresses.append(address)

        return addresses

    @staticmethod
    def _check(s: str) -> bool:
        if len(s) == 1 and "0" <= s <= "9":
            return True
        if len(s) == 2 and "10" <= s <= "99":
            return True
        if len(s) == 3 and "100" <= s <= "255":
            return True
        return False


if __name__ == '__main__':
    solution = Solution()

    answer = solution.restoreIpAddresses("25525511135")
    print(answer, ["255.255.11.135", "255.255.111.35"])

    answer = solution.restoreIpAddresses("0000")
    print(answer, ["0.0.0.0"])

    answer = solution.restoreIpAddresses("1111")
    print(answer, ["1.1.1.1"])

    answer = solution.restoreIpAddresses("010010")
    print(answer, ["0.10.0.10", "0.100.1.0"])

    answer = solution.restoreIpAddresses("101023")
    print(answer, ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
