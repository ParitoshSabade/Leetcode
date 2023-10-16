class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        total = 0
        prev = 0
        for letter in s:
            if roman_map[letter] > prev:
                total -= prev
                total += roman_map[letter] - prev
            else:
                total += roman_map[letter]
                
            prev = roman_map[letter]
            
        return total
            
            
        