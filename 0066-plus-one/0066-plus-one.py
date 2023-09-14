class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        flag = True
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                flag = False
                break
            else:
                digits[i] = 0
                
        if flag:
            digits.append(1)
            digits.reverse()
        return digits
                
                