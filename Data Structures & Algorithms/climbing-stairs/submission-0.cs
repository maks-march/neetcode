public class Solution {
    public int ClimbStairs(int n) {
        var dp = new int[n+1];

        for (int i = 0; i <= n; i++) {
            if (i < 2) dp[i] = 1;
            else if (i == 2) dp[i] = 2;
            else dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}