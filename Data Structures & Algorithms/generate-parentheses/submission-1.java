class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> res = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        dfs(0, 0, res, sb, n);
        return res;
    }

    private void dfs(int open, int close, List<String> res, StringBuilder cur, int n) {
        if (cur.length() == n * 2) {
            res.add(cur.toString());
            return;
        }

        if (open < n) {
            cur.append('(');
            dfs(open + 1, close, res, cur, n);
            cur.deleteCharAt(cur.length() - 1);
        }

        if (close < open) {
            cur.append(')');
            dfs(open, close + 1, res, cur, n);
            cur.deleteCharAt(cur.length() - 1);
        }
    }
}
