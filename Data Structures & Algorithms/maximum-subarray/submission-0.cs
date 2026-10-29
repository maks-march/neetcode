public class Solution {
    public int MaxSubArray(int[] nums) {
        var dp = new int[nums.Length];
        dp[0] = nums[0];
        var max = nums[0];
        for (int i = 1; i < nums.Length; i++) {
            dp[i] = Math.Max(nums[i], dp[i-1] + nums[i]);
            max = Math.Max(max, dp[i]);
        }
        return max;
    }
}