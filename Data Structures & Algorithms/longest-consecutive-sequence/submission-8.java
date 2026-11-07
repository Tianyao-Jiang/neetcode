class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();

        for (int num: nums) {
            set.add(num);
        }

        int res = 0;

        for (int i = 0; i < nums.length; i++) {
            if (!set.contains(nums[i] - 1)) {
                int cur = nums[i] + 1;
                int count = 1;
                while (set.contains(cur)) {
                    count++;
                    cur = cur + 1;
                }

                res = Math.max(res, count);
            }
        }

        return res;
    }
}
