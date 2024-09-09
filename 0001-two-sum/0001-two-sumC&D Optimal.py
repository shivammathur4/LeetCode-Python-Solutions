class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        hashmap=dict()
        for i in range(0,n):
            rem = target - nums[i]
            if rem in hashmap:
                return [hashmap[rem], i]
            hashmap[nums[i]] = i


        