""" Merge Sort
"""


def _merge(data, left, right, memeory):

    mid = int((left + right) / 2)
    left_ptr = left # (left ~ mid)
    right_ptr = mid + 1 # (mid + 1 ~ right)
    memory_ptr = 0
    while left_ptr <= mid and right_ptr <= right:
        if data[left_ptr] <= data[right_ptr]:
            memeory[memory_ptr] = data[left_ptr]
            left_ptr += 1
        else:
            memeory[memory_ptr] = data[right_ptr]
            right_ptr += 1
        memory_ptr += 1

    while left_ptr <= mid:
        memeory[memory_ptr] = data[left_ptr]
        left_ptr += 1
        memory_ptr += 1

    while right_ptr <= right:
        memeory[memory_ptr] = data[right_ptr]
        right_ptr += 1
        memory_ptr += 1

    # Copy
    for i in range(right - left + 1):
        data[left + i] =  memeory[i]
    return


def merge_sort(data, left, right, memory):

    # Base case
    if left == right:
        return

    # Divide
    mid = int((left + right) / 2)
    merge_sort(data, left, mid, memory)
    merge_sort(data, mid+1, right, memory)

    # Merge
    _merge(data, left, right, memory)
    return
