class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum=0
        roman_numerals = {
            "I": 1, "IV": 4, "V": 5,"IX": 9, "X": 10,"XL": 40, "L": 50,"XC": 90, "C": 100,"CD": 400, "D": 500,"CM":    900, "M": 1000
        }
        
        i=0
        while (i<len(s)):
            a = s[i]
            if(i<len(s)-1):
                double_char = s[i] + s[i + 1] 
                if double_char in roman_numerals:
                    i+=2
                    rm = roman_numerals.get(double_char)
                    sum+=rm
                    continue
            sum+=roman_numerals.get(a)
            i+=1
        return sum

            
