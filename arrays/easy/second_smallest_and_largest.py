def find_second_largest(arr,n):
    if n == 0 or n==1:
        print(-1,-1)
        return
    large = float('-inf')
    small = float('inf')
    for i in range(n):
        large = max(large,arr[i])
        small = min(small,arr[i])
    second_small = float('inf')
    second_large = float('-inf')
    for i in range(n):
        if(arr[i]!=large):
            second_large = max(second_large,arr[i])
        if(arr[i]!=small):
            second_small = min(second_small,arr[i])
    print("second_large is",second_large)
    print("second_small is ",second_small)

if __name__ =="__main__":
    arr = [1,5,1,3,8,6,7]
    n = len(arr)
    print("length of array is ",n)
    find_second_largest(arr,n)