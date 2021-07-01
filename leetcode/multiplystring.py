def multiplystrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """
    if num1 == '0' or num2 == '0':
        return '0'
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num1 = num1[::-1]
    num2 = num2[::-1]
    res = [0]*(len(num1)+len(num2))
    for i in range(len(num1)):
        for j in range(len(num2)):
            mult = int(num1[i])*int(num2[j])+res[i+j]
            res[i+j] = mult%10
            res[i+j+1] += mult//10
    for i in range(len(res)):
        res[i]=str(res[i])
    if res[len(res)-1] =='0':
        res = res[:len(res)-1]
    res = ''.join(res)
    return res[::-1]
print(multiplystrings('123', '456'))