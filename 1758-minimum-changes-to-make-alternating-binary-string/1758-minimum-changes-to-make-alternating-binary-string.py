class Solution:
    def minOperations(self, s: str) -> int:
        alt1 = ""
        alt2= ""
        for i in range(len(s)):
            if i%2 == 0:
                alt1 += "0"
                alt2 += "1"
            else:
                alt1 += "1"
                alt2 += "0"

        cnt1 = 0
        cnt2 = 0
        for i in range(len(s)):
            cnt1 += int(alt1[i])^int(s[i])
            cnt2 += int(alt2[i])^int(s[i])
        
        return min(cnt1,cnt2)