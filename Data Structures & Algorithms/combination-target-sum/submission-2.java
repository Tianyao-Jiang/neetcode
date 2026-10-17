class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();

        List<Integer> path = new ArrayList<>();

        dfs(nums, res, path, target, 0);
        return res;
    }

    private void dfs(int[] nums, List<List<Integer>> res, List<Integer> path, int target, int index) {
        if (target == 0) {
            res.add(new ArrayList<>(path));
            return;
        }

        if (target < 0) {
            return;
        }

        for (int i = index; i < nums.length; i++) {
            path.add(nums[i]);
            dfs(nums, res, path, target - nums[i], i);
            path.remove(path.size() - 1);
        }
    }
}
