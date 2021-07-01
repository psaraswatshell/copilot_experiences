def longestpalindromesubstring(str):
    if not str:
        return ""
    res = ""
    for i in range(len(str)):
        # odd case
        tmp = helper(str, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case
        tmp = helper(str, i, i + 1)
        if len(tmp) > len(res):
            res = tmp
    return res
def helper(str, l, r):
    while l >= 0 and r < len(str) and str[l] == str[r]:
        l -= 1; r += 1
    return str[l + 1:r]
print(longestpalindromesubstring("abacdfgdcaba"))
