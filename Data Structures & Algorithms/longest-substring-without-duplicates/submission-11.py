class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        _set = set()

        l = 0
        r = 0 

        while r < len(s):
        
            if s[r] not in _set:
                _set.add(s[r])
                r += 1
                res = max(res, len(_set))

            else:
                _set.remove(s[l])
                l += 1

        return res
                
            

                
            


            
