"""Quick Sort
"""


def quick_sort(data, left, right):

    # Base case
    if left >= right:
        return

    pivot = data[right]
    left_ptr = left
    right_ptr = right - 1
    while left_ptr <= right_ptr:
        if data[left_ptr] > pivot > data[right_ptr]:
            tmp = data[left_ptr]
            data[left_ptr] = data[right_ptr]
            data[right_ptr] = tmp
            left_ptr += 1
            right_ptr -= 1
        else:
            if data[left_ptr] <= pivot:
                left_ptr += 1
            if data[right_ptr] >= pivot:
                right_ptr -= 1

    # Exchange pivot and left_ptr
    tmp = data[left_ptr]
    data[left_ptr] = pivot
    data[right] = tmp

    quick_sort(data, left, left_ptr - 1)
    quick_sort(data, left_ptr + 1, right)
    return




