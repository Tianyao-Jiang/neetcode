class Solution {
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> comb = new ArrayList<>();
        dfs(n, k, res, comb, 1);
        return res;
    }

    private void dfs(int n, int k, List<List<Integer>> res, List<Integer> comb, int i) {
        if (k == 0) {
            res.add(new ArrayList<>(comb));
            return;
        }

        for (int j = i; j <= n; j++) {
            comb.add(j);
            dfs(n, k - 1, res, comb, j + 1);
            comb.remove(comb.size() - 1);
        }
    }
}