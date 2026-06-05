#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated

#brute force with n^2 complexity
class Solution:
    def check(nums):
        n = len(nums)
        for rotation_offset in range(n):
            temp_arr = []
            for i in range(rotation_offset,n):
                temp_arr.append(nums[i])
            for i in range(rotation_offset):
                temp_arr.append(nums[i])
            
            isSorted = True
            for i in range(1,n):
                if(temp_arr[i]<temp_arr[i-1]):
                    isSorted = False
                    break
            if isSorted:
                return True
        return False

#compare with sorted array with n^2 complexity
class Solution:
    def check(nums):
        n = len(nums)
        sorted_arr = sorted(nums)
        for rotation_offset in range(n):
            isMatch = True
            for index in range(n):
                if(nums[(rotation_offset+index)%n] != sorted_arr[index]):
                    isMatch = False
                    break
            if isMatch:
                return True
        return False
    
#optimal approach with n complexity -> counting inversion pairs

class Solution:
    def check(nums):
        n=len(nums)

        inversion_count = 0
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                inversion_count+=1
            if inversion_count>1:
                return False
        if(nums[0]<nums[n-1]):
            inversion_count+=1
        return inversion_count<=1

        