import random
import time

def exchange_sort(data):
    """Sort the data in ascending order using exchange sort.

    Input:
        data (list) : list of data.
    Returns:
        nothing.
    """

    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] > data[j]:
                tmp = data[i]
                data[i] = data[j]
                data[j] = tmp

def merge_sort(data):
    """Sort the data in ascending order using merge sort.

    Input:
        data (list) : list of data.
    Returns:
        nothing.
    """

    def _merge_sort(left, right):
        if left == right:
            return

        mid = int((left + right) / 2)
        #print("left: {}, right: {}, mid: {}".format(left, right, mid))
        _merge_sort(left, mid)
        _merge_sort(mid+1, right)

        tmp = [-1] * (right - left + 1)
        left_ptr = left
        right_ptr = mid+1
        tmp_ptr = 0
        while left_ptr <= mid or right_ptr <= right:
            if right_ptr > right:
                tmp[tmp_ptr] = data[left_ptr]
                left_ptr += 1
            elif left_ptr > mid:
                tmp[tmp_ptr] = data[right_ptr]
                right_ptr += 1
            elif data[left_ptr] < data[right_ptr]:
                tmp[tmp_ptr] = data[left_ptr]
                left_ptr += 1
            elif data[left_ptr] >= data[right_ptr]:
                tmp[tmp_ptr] = data[right_ptr]
                right_ptr += 1
            else:
                raise Exception("Error in while loop")

            tmp_ptr += 1

        for i in range(len(tmp)):
            data[left + i] = tmp[i]

    _merge_sort(0, len(data)-1)


num_of_data = 10
data = [] # range(1 ~ 1000)
for i in range(num_of_data):
    data.append(random.randint(1,1000))

print("[Exchange sort]")
random.shuffle(data)
print("Original data: ", data[:10], "...")
exchange_start_time = time.time()
exchange_sort(data)
print("Elapsed time for exchange sort: {}".format(time.time() - exchange_start_time))
print("Sorted data: ", data[:10], "...")

print("\n[Merge sort]")
random.shuffle(data)
print("Original data: ", data[:10], "...")
merge_start_time = time.time()
merge_sort(data)
print("Elapsed time for merge sort: {}".format(time.time() - merge_start_time))
print("Sorted data: ", data[:10], "...")
