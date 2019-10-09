class Solution:
    def convert(self, s, numRows):
        
        
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = []
        i = 0
        while i < numRows:
            rows.append("")
            i += 1
        rev = True
        curRow = 0
        high = numRows - 1
        for char in s:
            rows[curRow] += char
            if curRow == 0 or curRow == high:
                rev = not rev
            
            if rev:
                curRow -= 1
            else:
                curRow += 1
        rStr = ''
        for row in rows:
            rStr += row
        return rStr