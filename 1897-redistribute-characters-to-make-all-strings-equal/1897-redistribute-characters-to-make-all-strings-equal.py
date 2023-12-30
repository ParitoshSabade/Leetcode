class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        answer = True
        charCount = {}
        for word in words:
            for ch in word:
                if ch in charCount:
                    charCount[ch] += 1
                else:
                    charCount[ch] = 1
                
        counts = charCount.values()
        minCount = len(words)
        
        for cnt in counts:
            if cnt % minCount != 0:
                answer = False
                break
        
        return answer