class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        limit = min(len(word1),len(word2))
        res = ""
        for i in range(limit):
            res += word1[i] + word2[i]
        i+=1
        if len(word1) == len(word2):
            return res
        if len(word1) > len(word2):
            word = word1
        else:
            word = word2
        for j in range(i,len(word)):
            res+=word[j]
        return res
