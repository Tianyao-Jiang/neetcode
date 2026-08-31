class Solution {
    public int subsetXORSum(int[] nums) {
        int[] res = new int[1];
        List<Integer> subset = new ArrayList<>();
        dfs(nums, 0, res, subset);
        return res[0];
    }

    private void dfs(int[] nums, int i, int[] res, List<Integer> subset) {
        if (i >= nums.length) {
            int cur = 0;
            for (int j = 0; j < subset.size(); j++) {
                cur = cur ^ subset.get(j);
            }
            res[0] += cur;
            return;
        }

        subset.add(nums[i]);
        dfs(nums, i + 1, res, subset);

        subset.remove(subset.size() - 1);
        dfs(nums, i + 1, res, subset);
    }
}