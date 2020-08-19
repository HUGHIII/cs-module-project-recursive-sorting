# TO-DO: complete the helper function below to merge 2 sorted arrays

# mergedarr = [0,0,0,0,0,0,0,0,0,0]
# loop through each index compare each element of the array arguements to each other and insert
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    a,b = 0,0

    for item in range(elements):
        if a >= len(arrA):
            merged_arr[item] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[item] = arrA[a]
            b += 1
        elif arrA[a] < arrB[b]:
            merged_arr[item] = arrA[a]
            a += 1
        else:
            merged_arr[item] = arrB[b]
            b += 1



    return merged_arr
    
    
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]
print(merge(l1,l2))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    # base case
    if len(arr) > 1:
        # rec case
        # recursively split array until each list has len 1
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])

        # call merge func and pass sub arrs
        arr = merge(left, right)

    return arr



# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

