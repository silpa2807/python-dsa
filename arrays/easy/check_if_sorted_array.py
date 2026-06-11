#https://takeuforward.org/data-structure/check-if-an-array-is-sorted

#leetcode link is 
#https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/


#brute force for with n^2 complexity

def isSorted(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[j]<arr[i]:
                return False
    return True
if __name__ == "__main__":
    print("check if array is sorted in increasing order")
    arr=[1,1,2,3,3,4,5]
    n = len(arr)
    sorted = isSorted(arr,n)
    print("sorted is ",sorted)

#optimal approach with n complexity
#jzt check if current elment is smaller than prev element

def isSorted(arr,n):
    if n == 1:
        return True
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True

if __name__ == "__main__":
    print("check if array is sorted in increasing order")
    arr=[1,3,2,3,3,4,5]
    n = len(arr)
    sorted = isSorted(arr,n)
    print("sorted is ",sorted)






