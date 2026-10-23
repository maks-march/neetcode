public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
        var result = new List<List<int>>();
        Array.Sort(nums);
        for (int i = 0; i < nums.Length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            var l = i + 1;
            var r = nums.Length-1;
            while (l < r) {
                var total = nums[i] + nums[l] + nums[r];
                if (total == 0) {
                    result.Add([nums[i], nums[l], nums[r]]);
                    l++;
                    r--;
                    while (l < r && nums[l] == nums[l-1]) l++;
                    while (l < r && nums[r] == nums[r+1]) r--;
                }
                else if (total > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return result;
    }
}