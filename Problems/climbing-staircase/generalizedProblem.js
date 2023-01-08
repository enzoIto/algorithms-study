function climbingStaircase(n, X) {
  const dp = new Array(n+1).fill(0)
  dp[0] = 1
  for (let i = 1; i <= n; i++) {
    for (const x of X) {
      if (i - x >= 0) {
        dp[i] += dp[i-x];
      }
    }
  }
  return dp[0]
}