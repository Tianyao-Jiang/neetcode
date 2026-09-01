class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> subset = new ArrayList<>();

        dfs(nums, res, subset, 0);
        return res;
    }

    private void dfs(int[] nums, List<List<Integer>> res, List<Integer> subset, int i) {
        if (i >= nums.length) {
            res.add(new ArrayList<>(subset));
            return;
        }

        subset.add(nums[i]);
        dfs(nums, res, subset, i + 1);
        subset.remove(subset.size() - 1);
        while (i + 1< nums.length && nums[i] == nums[i+1]){
            i++;
        }
        dfs(nums, res, subset, i + 1);
    }
}
