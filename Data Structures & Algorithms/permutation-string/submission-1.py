class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        for c in s1:
            count1[c] = count1.get(c, 0) + 1

        have = 0
        need = len(count1)

        window = {}

        l = 0
        r = 0 

        while r < len(s2):
            c = s2[r]
            window[c] = window.get(c, 0) + 1

            if c in count1:
                if window.get(c) == count1[c]:
                    have += 1
                elif window.get(c) == count1[c] + 1:
                    have -= 1

            if r - l + 1 >len(s1):
                d = s2[l]
                if d in count1:
                    if window[d] == count1[d]:
                        have -= 1            # about to drop below target
                    elif window[d] == count1[d] + 1:
                        have += 1            # about to come back to target
                window[d] -= 1
                l += 1


            if have == need:
                return True

            r += 1

        return False



        


            
