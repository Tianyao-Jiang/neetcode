class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        res = []

        l = 0
        r = len(numbers) - 1

        while l < r:
            temp = numbers[l] + numbers[r]

            if temp < target:
                l += 1
            elif temp > target:
                r -= 1
            else:
                res.append(l + 1)
                res.append(r + 1)
                break

        return res