public class Solution {
    public int ClimbStairs(int n) {
        var first = 1;
        var second = 2;

        for (int i = 3; i <= n; i++) {
            first += second;
            second = first - second;
            first = first - second;
            second = first + second;
        }
        return n == 1 ? first : second;
    }
}