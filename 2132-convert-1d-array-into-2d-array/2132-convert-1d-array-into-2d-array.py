class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        j = 0
        answer = []
        for i in range(m):
            row = []
            limit = (i+1)*n

            while j < limit:
                row.append(original[j])
                j+=1
            answer.append(row)
        return answer