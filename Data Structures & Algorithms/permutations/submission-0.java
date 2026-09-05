class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> cur = new ArrayList<>();
        boolean[] selected = new boolean[nums.length];
        dfs(nums, selected, res, cur);
        return res;

    }

    private void dfs(int[] nums, boolean[] selected, List<List<Integer>> res, List<Integer> cur) {

        if (cur.size() == nums.length) {
            res.add(new ArrayList(cur));
        }

        for (int i = 0; i < nums.length; i++) {
            if (!selected[i]) {
                cur.add(nums[i]);
                selected[i] = true;
                dfs(nums, selected, res, cur);
                cur.remove(cur.size() - 1);
                selected[i] = false;
            }
        }
    }
}
