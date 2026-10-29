public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        var minLength = nums.Length + 1;
        var l = 0;
        var sum = nums[0];
        if (sum >= target) return 1;

        for (int r = 1; r < nums.Length; r++) {
            sum += nums[r];
            while (sum >= target) {
                minLength = Math.Min(minLength, r-l+1);
                sum -= nums[l];
                l++;
            }
        }
        return minLength <= nums.Length ? minLength : 0;
    }
}