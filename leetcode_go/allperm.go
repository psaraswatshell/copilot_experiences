func distinctsubstringscount(s string) int {
    if s == "" {
        return 0
    }
    n := len(s)
    dp := make([]int, n+1)
    dp[0] = 1
    for i := 1; i <= n; i++ {
        for j := i - 1; j >= 0; j-- {
            if s[j] != s[i-1] {
                dp[i] += dp[j]
            }
        }
    }
    return dp[n]
}