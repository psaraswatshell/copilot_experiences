func permute(nums []int) [][]int {
    var res [][]int
    dfs(&res, nums, 0)
    return res
}

func dfs(res *[][]int, nums []int, start int){
    if start >= len(nums){
        t := make([]int, len(nums))  //be careful of these two lines
        copy(t, nums)
        *res = append(*res, t)
        return
    }
    for i := start; i < len(nums); i++{
        nums[start], nums[i] = nums[i], nums[start]
        dfs(res, nums, start+1)
       nums[start], nums[i] = nums[i], nums[start]
    }
}