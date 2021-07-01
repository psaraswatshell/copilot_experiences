def distinctsubstringscount(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    res = set()
    for i in range(len(s)):
        for j in range(i, len(s)):
            res.add(s[i:j + 1])
    return len(res)