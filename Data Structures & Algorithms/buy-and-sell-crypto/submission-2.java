class Solution {
    public int maxProfit(int[] prices) {
        int l = 0;
        int r = 0;
        int curMax = 0;

        // r finds the highest
        // l finds the lowest;
        while(r < prices.length) {
            if (prices[r] < prices[l]) {
                l = r;
            } else {
                curMax = Math.max(curMax, prices[r] - prices[l]);
            }
            r++;
        }
        return curMax;
    }
}
