# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    i = 0
    j = 0
    for k in range(elements):
        if i == len(arrA):
            merged_arr[k] = arrB[j]
            j += 1
        elif j == len(arrB):
            merged_arr[k] = arrA[i]
            i += 1
        elif arrA[i] >= arrB[j]:
            merged_arr[k] = arrB[j]
            j += 1
        elif arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # check if the array's length is 1 or less. If so, return the list
    if len(arr) <= 1:
        return arr
    #divide in half
    mid = len(arr)//2
    L = arr[:mid]
    R = arr[mid:]

    # print(f"L:{L}\nR:{R}")
    sorted_L = merge_sort(L)
    sorted_R = merge_sort(R)
    # print(f"sorted_L:{sorted_L}\nsorted_R:{sorted_R}")
    merged = merge(sorted_L, sorted_R)
    # print(f"merged:{merged}")
    return merged


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
        # TO-DO
    left = arr[start:mid]
    right = arr[mid:end+1]
    print(f"right{right}")
    print(f"left {left}")

    i = 0
    j = 0
    for k in range(start, end+1):
        if i == len(left):
            arr[k] = right[j]
            j += 1
        elif j == len(right):
            arr[k] = left[i]
            i += 1
        elif left[i] >= right[j]:
            arr[k] = right[j]
            j += 1
        elif left[i] < right[j]:
            arr[k] = left[i]
            i += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


# Challenge from class
def rec(arr, x, i):
    if i >= 0:
        if arr[i] == x:
            return True
        else:
            return rec(arr, x, i-1)
    return False


# a = [2, 3, 5, 67, 8]
# n = len(a)-1
# print(rec(a, 67, n))
# print(rec(a, 4, n))

print(merge_sort([1, 3, 2, 190, 1, -1]))
# print(merge([1], [3, 2]))
