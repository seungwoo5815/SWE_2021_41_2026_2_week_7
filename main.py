from typing import List

def twoSum (nums: List[int], target: int) -> List[int] :
    
    num_memo = {}
    
    for i, num in enumerate(nums) :
        diff = target - num

        if diff in num_memo:
            return [num_memo[diff], i]
        
        num_memo[num] = i
        
    return []
