public class Solution {
    public int MinSubArrayLen(int target, int[] nums) {
        var minLength = nums.Length + 1;
        var l = 0;
        var r = l+1;
        var sum = nums[0];
        if (sum >= target) return 1;

        while (l < nums.Length - 1) {
            while (sum < target && r < nums.Length) {
                sum += nums[r];
                r++;
            }
            if (sum < target) break;
            while (sum >= target && l < r) {
                minLength = Math.Min(r-l, minLength);
                sum -= nums[l];
                l++;
            }
        }
        return minLength <= nums.Length ? minLength : 0;
    }
}