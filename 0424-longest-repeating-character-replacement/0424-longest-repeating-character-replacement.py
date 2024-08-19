class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxOccur = 0
        for r in range(len(s)):
            if s[r] not in count:
                count[s[r]] = 0
            count[s[r]] += 1
            maxOccur = max(maxOccur,count[s[r]])
            maxLength = 0
            while r-l+1-maxOccur > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l+=1
            maxLength = max(maxLength,r-l+1)
        return maxLength