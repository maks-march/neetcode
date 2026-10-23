public class Solution {
    public List<List<int>> ThreeSum(int[] nums) {
                var result = new HashSet<(int, int, int)>();
        nums = nums.Order().ToArray();
        for (int i = 0; i < nums.Length - 2; i++) {
            var l = i + 1;
            var r = nums.Length-1;
            while (l < r) {
                var total = nums[i] + nums[l] + nums[r];
                if (total == 0) {
                    result.Add((nums[i], nums[l], nums[r]));
                }
                if (total > 0) {
                    r--;
                } else {
                    l++;
                }
            }
        }
        return result
            .Select(x => new List<int>() {x.Item1, x.Item2, x.Item3}).ToList();
    }
}
