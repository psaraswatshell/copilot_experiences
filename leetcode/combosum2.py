def combinationSum2(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    res = []
    def dfs(candidates, target, path, start): 
        if target < 0:
            return      
        if target == 0:       
            res.append(path)       
            return
        previous = -1       
        for i in range(start, len(candidates)):
            if previous!=candidates[i]: 
                dfs(candidates, target - candidates[i], path + [candidates[i]], i + 1)
                previous = candidates[i]
    dfs(candidates, target, [], 0)
    return res