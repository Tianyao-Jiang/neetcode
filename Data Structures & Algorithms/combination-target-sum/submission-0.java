class Solution {
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> combination = new ArrayList<>();

        dfs(nums, 0, res, combination, target);

        return res;
    }

    private void dfs(int[] nums, int i, List<List<Integer>> res, List<Integer> combination, int target) {
        int sum = 0;
        for (int j = 0; j < combination.size(); j++) {
            sum += combination.get(j);
        }
        if (sum == target) {
            res.add(new ArrayList<>(combination));
            return;
        }

        if (sum > target) {
            return;
        }

        if (i > nums.length - 1) {
            return;
        }

        combination.add(nums[i]);
        dfs(nums, i, res, combination, target);
        combination.remove(combination.size() - 1);
        dfs(nums, i + 1, res, combination, target);

    }
}
