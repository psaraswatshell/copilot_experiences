def zigzagconvert(s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        res = [[] for i in range(numRows)]
        i = 0
        flag = True
        for c in s:
            res[i].append(c)
            if i == 0:
                flag = True
            elif i == numRows - 1:
                flag = False
            if flag:
                i += 1
            else:
                i -= 1
        res = [''.join(i) for i in res]
        return ''.join(res)