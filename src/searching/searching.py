# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    arr.sort()
    if start > end:
        return False
    mid = (start + end)//2
    # on second pass of recursion the mid sets as 7 everytime which is end
    if target == arr[mid]:
        return True
    elif target < arr[mid]:
        return binary_search(arr,target,start,mid - 1)
    else:
        return binary_search(arr,target,mid + 1,end)
    
lst = [5,3,1,8,7,12,13,11]
target = 12

result = binary_search(lst,target,0,len(lst)-1)
if result is True:
    print(str(result))
else:
    print('target not present')

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

