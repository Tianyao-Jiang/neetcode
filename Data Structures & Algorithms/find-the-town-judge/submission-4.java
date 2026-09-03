class Solution {
    public int findJudge(int n, int[][] trust) {
        
        int[] incoming = new int[n+ 1];
        int[] outgoing = new int[n+ 1];

        for (int i = 0; i < trust.length; i++) {
            int[] node = trust[i];
            int in = node[1];
            int out = node[0];

            incoming[in] += 1;
            outgoing[out] += 1;
        }

        for (int i = 0; i < n + 1; i++) {
            if (incoming[i] == n - 1 && outgoing[i] == 0) {
                return i;
            }
        }

        return -1;
    }
}