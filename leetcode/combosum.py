def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    candidates.sort()
    res = []
    dfs(candidates, target, 0, [], res)
    return res
def dfs(candidates, target, index, path, res):       
    if target == 0:       
        res.append(path)       
        return       
    for i in range(index, len(candidates)):       
        if target < candidates[i]:       
            return       
        dfs(candidates, target - candidates[i], i, path + [candidates[i]], res)