class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count = {}
        for i in range(len(t)):
            count[t[i]] = count.get(t[i], 0) + 1
        missing = len(count)
        
        m = {}

        l = 0
        r = 0

        res = ""
        length = float("inf")
        best = (-1, -1)

        while r < len(s):
            m[s[r]] = m.get(s[r], 0) + 1
            
            if s[r] in count and m[s[r]] == count[s[r]]:
                missing -= 1

            while missing == 0:
                if r - l + 1 < length:
                    length = r - l + 1
                    best = (l, r)
                
                m[s[l]] -= 1
                if s[l] in count and m[s[l]] < count[s[l]]:
                    missing += 1
                l += 1

            r += 1 
        l, r = best
        return res if length == float("inf") else s[l: r+1]
