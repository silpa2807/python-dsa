#https://leetcode.com/problems/rotate-array/

#bruteforce approach where we create a temp array and put elements from the last rotation index to the temp array

# def rotate_by_k(nums,k):
#     n = len(nums)
#     temp = [0]*n

#     lri = n-k
#     j=0
#     for i in range(lri,n):
#         temp[j] = nums[i]
#         j+=1
#     for i in range(0,lri):
#         temp[j]=nums[i]
#         j+=1

#     nums[:] = temp
#     return nums


# if __name__ == "__main__":
#     print("starting function")
#     nums = [1,2,3,4,5,6,7]
#     k=3

#     temp = rotate_by_k(nums,k)
#     print("nums array is ",temp)


#brute force leetcode
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         temp = [0]*n

#         k = k%n

#         lri = n-k
#         j=0
#         for i in range(lri,n):
#             temp[j] = nums[i]
#             j+=1
#         for i in range(0,lri):
#             temp[j]=nums[i]
#             j+=1

#         nums[:] = temp

#optimal solution

def reverse(nums, start, end):
    while(start<end):
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start+=1
        end-=1


def rotate_by_k(nums,k):
    n = len(nums)

    reverse(nums,0,n-1)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
        
if __name__ == "__main__":
    print("starting the function")
    nums = [1,2,3,4,5,6,7]
    k=3
    rotate_by_k(nums,k)

    print("the roated array is ",nums)


#leetcode solution
class Solution:
    def reverse(self,nums, start, end):
        while(start<end):
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp
            start+=1
            end-=1

    
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k%=n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)
