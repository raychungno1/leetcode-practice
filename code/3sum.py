class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        length = len(nums)
        nums.sort() # Sort to group duplicate values
        
        for i, num in enumerate(nums):
            # Skip duplicates
            if i > 0 and num == nums[i - 1]: continue
            
            # Perform 2Sum algorithm on the rest of array
            # w/ target = -nums[i] and add the results
            for double in self.twoSumSorted(nums, -num, i + 1, length - 1):
                triplets.append([num] + double)
                
        return triplets
    
    def twoSumSorted(self, nums, target, l, r):
        result = []

        while l < r:
            total = nums[l] + nums[r]

            # If our candidate values are too big,
            # Decrement our right pointer to a smaller value
            if total > target:
                r -= 1

            # If our candidate values are too small,
            # Increment our left pointer to a bigger value  
            elif total < target:
                l += 1

            # Otherwise, we have found a valid tuple
            # Increment our left pointer to the next unique value
            else:
                result.append([nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                
        return result
        