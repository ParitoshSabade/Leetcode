class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sMap,tMap = {},{}
        cnt = 0
        for i in range(len(s)):
            if s[i] in sMap:
                sMap[s[i]]+=1
            else:
                sMap[s[i]] = 1
                
            if t[i] in tMap:
                tMap[t[i]]+=1
            else:
                tMap[t[i]] = 1
        # print(sMap)
        # print(tMap)
        for k in sMap.keys():
            if k in tMap:
                if sMap[k] > tMap[k]:
                    cnt += sMap[k] - tMap[k]
            else:
                cnt+=sMap[k]
        return cnt
                
            
                
            
                