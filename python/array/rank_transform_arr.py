class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        sorted_unique = sorted(set(arr))
        
        rank_dict = {}
        for rank, num in enumerate(sorted_unique):
            rank_dict[num] = rank + 1
        
        result = []
        for num in arr:
            result.append(rank_dict[num])
        
        return result
    