### 3Sum

Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

The solution set must not contain duplicate triplets.

---

<details>
<summary><b>Brute Force</b></summary>

Use a triple-loop to iterate through each index of the array, making sure that indexes are not repeated multiple times when iterating.

Inside the for loop, check if the values at all 3 indexes add up to 0; if they do, sort the values, and add the resulting triplet a HashSet (this is done to remove duplicates). 

Finally, convert this HashSet to an array. 

*Time: `O(n^3)`*
>The algorithm uses 3 nested loops with a constant time body. 

*Space: `O(n)`*
> There can never be more than `n` tuples that add to 0. 

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = set()
        l = len(nums)
        
        # Iterate through each combo of triplets
        for i in range(l):
            for j in range(i + 1, l):
                for k in range(j + 1, l):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                
        return [[i, j, k] for i, j, k in triplets]
```
</details>

---
<details>
<summary><b>Hint for Optimal Solution</b></summary>
  
For each element `x` in the array, find two other elements that add up to `-x`. Sorting the array allows us to remove duplicates, since we can compare if the element was iterated on previously with a check like `nums[i] == nums[i - 1]`

</details>

---
<details>
<summary><b>Optimal</b></summary>

First sort the array. This means that all duplicate values will be grouped together to remove duplicates. 

Now, iterate through the array using an index `i`, ensuring that duplicate elements are not repeated multiple times with a check like `nums[i] == nums[i - 1]`


Now we just have to perform a 2Sum algorithm on the remainder of the array (starting from index `i + 1`), searching for a target of `-nums[i]`. Since the array is now sorted, this can be done with a two pointer algorithm. 

From now on, we will refer to `-nums[i]` as `target`.

Start with a `left` pointer at `i + 1` and a `right` pointer at the end of the array.
* If `left + right > target`, we must decrement `right` by 1.
* If `left + right < target`, we must increment `left` by 1.
* Otherwise, we have found a unique tuple `[-target, nums[left], nums[right]]`. This time, we increment our left pointer, skipping over duplicates. 

*Time: `O(n^2)`*
>We first iterate through each value in the array, which is `O(n)`. In the body of each loop, we perform the 2Sum algorithm, which is also `O(n)`, resulting in `O(n^2)`. Sorting the array takes `O(log(n))`, which is asymptotically smaller than `O(n^2)`.

*Space: `O(n)`*
> Same as brute force solution.

```python
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
    
```

---