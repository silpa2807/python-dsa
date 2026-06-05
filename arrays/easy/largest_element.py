#https://takeuforward.org/data-structure/find-the-largest-element-in-an-array


def findLargest(arr,n):
    if n==0:
        print(-1)
    max_val = float('-inf')
    for i in range(n):
        max_val = max(max_val,arr[i])
    return max_val
   
    

if __name__ == "__main__":
    print("starting function")
    #even if there are duplicates
    arr = [2,1,5,5,5]
    n = len(arr)
    largest = findLargest(arr,n)
    print("largest element is",largest)

