# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    for i in range(len(arr)):
        print("arr", arr)
        last_index = len(arr)
        current = arr[i]

        # TODO: can I find index of the smallest element and the value at the same time, i.e in one loop?
        smallest = min(arr[i:last_index])
        smallest_index = arr.index(smallest)

        arr[i] = smallest
        arr[smallest_index] = current

        # for i in range(0, len(arr) - 1):
        # cur_index = i
        # smallest_index = cur_index

    return arr

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    # check first item
    # compare against neighbor
    # if swap happens continue
    # otherwise go to the next index
    for i in range(len(arr)):
        print("i", i)
        for j in range(len(arr)-1-i):
            print("j", j)
            if arr[j] > arr[j+1]:
                tmp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = tmp
                print("if arr", arr)

    return arr

    # STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr


list = [6, 2, 5, 4, 1, 3]
# print(bubble_sort(list))
print(selection_sort(list))
