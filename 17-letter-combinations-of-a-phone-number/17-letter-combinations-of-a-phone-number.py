class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dict_ = {'2': 'abc',
                 '3': 'def',
                 '4': 'ghi',
                 '5': 'jkl',
                 '6': 'mno',
                 '7': 'pqrs',
                 '8': 'tuv',
                 '9': 'wxyz'}
        sizes = []
        for digit in digits:
            sizes.append(len(dict_[digit]))
        enums = [0]*len(sizes)
        combs = []
        while True:
            i = len(enums) - 1
            while i > 0:
                if enums[i] == sizes[i]:
                    enums[i] = 0
                    enums[i-1] += 1
                i -= 1
            if enums[0] == sizes[0]:
                break
            comb = '' # initializes a combination
            for digit, enum in zip(digits, enums):
                comb += dict_[digit][enum]
            combs.append(comb)
            enums[-1] += 1
        return combs