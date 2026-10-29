public class Solution {
    public int CoinChange(int[] coins, int amount) {
        var hd = new int[amount+1];
        Array.Fill(hd, amount + 1);
        hd[0] = 0;
        for (int i = 1; i <= amount; i++) {
            
            foreach (var coin in coins) {
                if (coin <= i) {
                    hd[i] = Math.Min(hd[i], hd[i-coin]+1);
                }
            }
        }
        
        return hd[amount] > amount ? -1 : hd[amount];
    }
}
