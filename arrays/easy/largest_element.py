def findLargest(arr):
    max = arr[0]
    for num in arr:
        if(num>max):
            max=num
    return max

if __name__ == "__main__":
    print("Largest element in an array")
    arr = [2,1,3,5,4]
    largest = findLargest(arr)
    print("largest element is",largest)

