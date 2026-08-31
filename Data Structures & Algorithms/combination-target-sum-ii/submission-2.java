class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> comb = new ArrayList<>();
        Arrays.sort(candidates);
        dfs(candidates, target, res, comb, 0);
        return res;
    }

    private void dfs(int[] candidates, int target, List<List<Integer>> res, List<Integer> comb, int i) {
        if (target == 0) {
            res.add(new ArrayList<>(comb));
            return;
        }

        if (target < 0) {
            return;
        }

        if (i >= candidates.length) {
            return;
        }

        comb.add(candidates[i]);
        dfs(candidates, target - candidates[i], res, comb, i + 1);
        comb.remove(comb.size() -1);
        int j = i;
        while(j < candidates.length && candidates[j] == candidates[i]) {
            j++;
        }
        dfs(candidates, target, res, comb, j);
    }
}
