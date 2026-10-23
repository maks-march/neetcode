public class Solution {
    public int[] SortedSquares(int[] nums) {
        var st = new int[nums.Length];
        var l = 0;
        var r = nums.Length - 1;

        while (l <= r) {
            var left = nums[l] * nums[l];
            var right = nums[r] * nums[r];
            if (left > right) {
                st[r-l] = left;
                l++;
            }else {
                st[r-l] = right;
                r--;
            }
        }
        return st;
    }
}