class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        count = 0
        n = len(arr) / 2
        res = [(a, b) for idx, a in enumerate(arr) for b in arr[idx + 1:]]

        for item in res:
            if (item[0] + item[1]) % k == 0:
                count += 1
        
        return count >= n
    
