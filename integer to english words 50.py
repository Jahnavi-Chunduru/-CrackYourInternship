class Solution:
    def __init__(self):
        self.words = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }

    def convert(self, num: int) ->str:
        remaining = num
        ret = str()

        if remaining >= 100:
            q, r = divmod(remaining, 100)
            ret += self.words[q] + ' Hundred'
            remaining -= q*100
            if remaining > 0:
                ret += ' '
            
        if remaining >= 20:
            q, r = divmod(remaining, 10)
            ret += self.words[q*10]
            remaining -= q*10
            if remaining > 0:
                ret += ' '
            
        if remaining > 0:
            ret += self.words[remaining]

        return ret
        
    def numberToWords(self, num: int) -> str:
        remaining = num
        ret = ''
        
        if num == 0:
            ret = 'Zero'
        else:
            if remaining >= 1000000000:
                q = remaining // 1000000000
                ret += ' ' + self.convert(q) + ' Billion'
                remaining -= q*1000000000

            if remaining >= 1000000:
                q = remaining // 1000000
                ret += ' ' + self.convert(q) + ' Million'
                remaining -= q*1000000

            if remaining >= 1000:
                q = remaining // 1000
                ret += ' ' + self.convert(q) + ' Thousand'
                remaining -= q*1000
        
            if remaining > 0:
                ret += ' '
                ret += self.convert(remaining)
        
        return ret.strip()
