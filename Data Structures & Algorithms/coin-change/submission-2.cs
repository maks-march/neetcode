public class Solution {
    public int CoinChange(int[] coins, int amount) {
        if (amount == 0) return 0;
        var hd = new int[amount+1];
        for (int i = 1; i <= amount; i++) {
            
            foreach (var coin in coins) {
            if (coin <= i && (i-coin == 0 || hd[i-coin] > 0) ) {
                    hd[i] = hd[i] == 0 ? hd[i-coin] + 1 : Math.Min(hd[i], hd[i-coin]+1);
                }
            }
        }
        
        return hd[amount] == 0 ? -1 : hd[amount];
    }
}
