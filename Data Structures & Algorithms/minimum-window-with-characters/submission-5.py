class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        countT = {}
        window = {}

        l = 0
        r = 0

        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1

        have = 0 
        need = len(countT)

        res = [-1, -1]
        resLen = float("inf")

        while r < len(s):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and countT[c] == window[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res[0] = l
                    res[1] = r

                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        
            r += 1

        l, r = res

        return s[l: r + 1] if resLen != float("inf") else ""





