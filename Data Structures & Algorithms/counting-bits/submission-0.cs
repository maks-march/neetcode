public class Solution {
    public int[] CountBits(int n) {
        var dp = new int[n+1];
        var offset = 1;
        for (int i = 1; i < n + 1; i++) {
            if (offset * 2 == i) {
                offset *= 2;
            }
            dp[i] = 1 + dp[i - offset];
        }
        return dp;
    }
}
