class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        #get M's
        fig = num // 1000
        if fig > 0:
            num = num % (1000*fig)
            for _ in range(fig):
                roman += "M"
        fig = num // 100
        if fig > 0:
            num = num % (100*fig)
            if fig == 4:
                roman += "CD"
            elif fig == 9:
                roman += "CM"
            else:
                if fig >= 5:
                    roman += "D"
                    fig -= 5
                while fig > 0:
                    roman += "C"
                    fig -= 1
        
        fig = num // 10
        if fig > 0:
            num = num % (10*fig)
            if fig == 4:
                roman += "XL"
            elif fig == 9:
                roman += "XC"
            else:
                if fig >= 5:
                    roman += "L"
                    fig -= 5
                while fig > 0:
                    roman += "X"
                    fig -= 1
        if num == 4:
            roman += "IV"
        elif num == 9:
            roman += "IX"
        else:
            if num >= 5:
                roman += "V"
                num -= 5
            while num > 0:
                roman += "I"
                num -= 1
        return roman