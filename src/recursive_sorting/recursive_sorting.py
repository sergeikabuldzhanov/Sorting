# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    if len(arrA) == 0:
        return arrB
    elif len(arrB) == 0:
        return arrA
    for i in range(elements):
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] > arrB[0]:
            merged_arr[i] = arrB.pop(0)

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr
    else:
        middle = len(arr)//2
        return merge(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO
    arr1 = arr[start:mid+1]
    arr2 = arr[mid+1:end+1]
    arr1_index = 0
    arr2_index = 0
    sorted_index = start
    while arr1_index < len(arr1) and arr2_index < len(arr2):
        # If our arr1 has the smaller element, put it in the sorted
        # part and then move forward in arr1 (by increasing the pointer)
        if arr1[arr1_index] <= arr2[arr2_index]:
            arr[sorted_index] = arr1[arr1_index]
            arr1_index = arr1_index + 1
        # Opposite from above
        else:
            arr[sorted_index] = arr2[arr2_index]
            arr2_index = arr2_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in arr1 or arr2
    # so we will go through the remaining elements and add them
    while arr1_index < len(arr1):
        arr[sorted_index] = arr1[arr1_index]
        arr1_index = arr1_index + 1
        sorted_index = sorted_index + 1

    while arr2_index < len(arr2):
        arr[sorted_index] = arr2[arr2_index]
        arr2_index = arr2_index + 1
        sorted_index = sorted_index + 1


def merge_sort_in_place(arr, l, r):
    # TO-DO
    if l >= r:
        return arr
    middle = (l+r)//2
    merge_sort_in_place(arr, l, middle)
    merge_sort_in_place(arr, middle+1, r)
    merge_in_place(arr, l, middle, r)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
