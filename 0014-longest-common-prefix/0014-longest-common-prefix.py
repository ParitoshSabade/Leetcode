class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Check if the input list is empty
            return ""
        
        start = strs[0]
        mnCount = len(start)

        for i in range(1, len(strs)):
            cnt = 0

            # Compare characters only up to the length of the shortest string
            for j in range(min(len(strs[i]), len(start))):
                if strs[i][j] == start[j]:
                    cnt += 1
                else:
                    break

            mnCount = min(mnCount, cnt)

        return start[:mnCount]
        