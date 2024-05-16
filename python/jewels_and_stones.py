# First solution accepted.
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_count = 0
        jewel_set = set(jewels)
        for stone in stones:
            if stone in jewel_set:
                jewel_count += 1

        return jewel_count
    

def num_jewels_in_stones(jewels: str, stones: str) -> int:
    count = 0
    for i in stones:
        if i in jewels:
            count+=1
    return count