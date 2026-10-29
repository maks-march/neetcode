public class Solution {
    public bool ContainsNearbyDuplicate(int[] nums, int k) {
        if (k >= nums.Length) {
            k = nums.Length - 1;
        }
        var hs = new HashSet<int>();
        for (int i = 0; i < nums.Length; i++) {
            if (hs.Contains(nums[i]))
                return true;
            hs.Add(nums[i]);
            if (hs.Count > k) {
                hs.Remove(nums[i-k]);
            }
        }
        return false;
    }
}