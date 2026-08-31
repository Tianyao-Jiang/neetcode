class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> curRes = new ArrayList<>();
        dfs(res, curRes, 0, nums);

        return res;
    }

    private void dfs(List<List<Integer>> res, List<Integer> curRes, int cur, int[] nums) {

        // for each node, check if it is leave
        if (cur >= nums.length) {
            res.add(new ArrayList<>(curRes));
            return;
        }

        // left put
        curRes.add(nums[cur]);
        dfs(res, curRes, cur + 1, nums);

        // right no put
        curRes.remove(curRes.size() - 1);
        dfs(res, curRes, cur + 1, nums);
    }
}
