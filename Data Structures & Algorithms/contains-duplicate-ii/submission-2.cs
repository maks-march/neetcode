public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        if (k >= nums.Length) {
            k = nums.Length - 1;
        }
        var hd = new Dictionary<int, int>();
        for (int i = 0; i < nums.Length; i++) {
            if (hd.ContainsKey(nums[i]) && i - hd[nums[i]] <= k)
                return true;
            hd[nums[i]] = i;
        }
        return false;
    }
}