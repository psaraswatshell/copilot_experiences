def letterCombinationsPhoneAll(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if len(digits) == 0:
        return []
    dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    for i in digits:
        if len(res) == 0:
            for j in dic[i]:
                res.append(j)
        else:
            tmp = []
            for j in dic[i]:
                for k in res:
                    tmp.append(k + j)
            res = tmp
    return res

print(letterCombinationsPhoneAll('23'))