class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        prev = 100000
        for letter in s:
            if roman_map[letter] <= prev:
                value += roman_map[letter]
                prev = roman_map[letter]
            else:
                value = value - prev
                value = value + roman_map[letter] - prev
                
        return value
            