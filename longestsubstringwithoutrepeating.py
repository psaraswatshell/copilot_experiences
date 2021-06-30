def longestsubstringwithoutrepeated(s):
    if not s:
        return 0
    res = 0
    for i in range(len(s)):
        j = i
        while j < len(s) and s[j] not in s[i:j]:
            j += 1
        res = max(res, j-i)
    return res