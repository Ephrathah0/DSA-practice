class Solution:
    def numberToWords(self, num: int) -> str:
        units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        ten = {10 : 'Ten',
          11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen',
          15 : 'Fifteen', 16 : 'Sixteen', 17 : 'Seventeen', 18 : 'Eighteen',
          19 : 'Nineteen'}
        tens = [0,0,'Twenty', "Thirty", "Forty", "Fifty", "Sixty", "Seventy", 'Eighty', 'Ninety']
        hunds = {
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }
        
        l = len(str(num))
        q, mod = divmod(num, 10**(l-1))
        if l == 1:
            return units[num]
            
        elif l == 2:
            if num > 9 and num < 20:
                return ten[num]
            unit = " "
            if mod != 0:
                unit = " " + self.numberToWords(mod)
            
            res = tens[q] + unit
            res = ' '.join(res.split())
            return res
        elif l > 2:
            if l > 3 and l < 7:
                l = 4
            elif l > 6 and l < 10:
                l = 7
            q, mod = divmod(num, 10**(l-1))
            res = ''
            if mod != 0:
                res = ' ' + self.numberToWords(mod)
            return self.numberToWords(q) + " " + hunds[10**(l-1)]  + res