class Solution:
    def intToRoman(self, val: int) -> str:
        divisors = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

        pointer = 0
        result = ''

        while val:
            d, symbol = divisors[pointer]
            rem = val % d
            if rem != val:
                result += symbol
                val -= d
            else:
                pointer += 1

        return result