class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i] == nums[ i - 1]) {
                continue;
            }

            int l = i + 1;
            int r = nums.length - 1;

            while(l < r) {
                int cur = nums[l] + nums[r] + nums[i];

                if (cur > 0) {
                    r--;
                } else if (cur < 0) {
                    l++;
                } else {
                    res.add(Arrays.asList(nums[l], nums[r], nums[i]));
                    l++;
                    r--;
                    while(l < r && nums[l] == nums[l - 1]){
                        l++;
                    }

                   
                }
            }
        }

        return res;
    }
}
