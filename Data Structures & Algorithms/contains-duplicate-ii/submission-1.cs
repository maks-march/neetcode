public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        if (k >= nums.Length) {
            k = nums.Length - 1;
        }
        for (int i = 0; i < nums.Length - k; i++) {
            var hs = new HashSet<int>();
            for (int j = i; j <= i + k; j++) {
                if (hs.Contains(nums[j])) {
                    return true;
                }
                hs.Add(nums[j]);
            }
        }
        return false;
    }
}