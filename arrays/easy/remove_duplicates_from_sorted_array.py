#https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array

#leetcode
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

#write down the explanation

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        k=0
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                k+=1
                nums[k]=nums[i+1]
        
        return k+1



        