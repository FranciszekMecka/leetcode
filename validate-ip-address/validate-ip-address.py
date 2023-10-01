class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count(".") == 3:  # IPv4
            queryIP = queryIP.split(".")
            for i in queryIP:
                if len(i) < 1 or len(i) > 3:
                    return "Neither"
                for j in i:
                    if ord(j) > 57 or ord(j) < 48:
                        return "Neither"
                if int(i) > 255 or int(i) < 0:
                    return "Neither"
                if int(i[0]) == 0 and len(i) > 1:
                    return "Neither"
            return "IPv4"
        if queryIP.count(":") == 7:  # IPv6
            queryIP = queryIP.split(":")
            for i in queryIP:
                if len(i) < 1 or len(i) > 4:
                    return "Neither"
                for j in i:
                    if (ord(j) - ord('0') < 0 or ord(j) - ord('0') > 9) and (j.lower() < 'a' or j.lower() > 'f'):
                        return "Neiither"
            return "IPv6"
        else:
            return "Neither"


print(Solution().validIPAddress("1.0.1."))
