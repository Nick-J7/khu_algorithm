import company


# recursive
def bin_search(data, item, left, right):

    # Base case: Not found
    if left > right:
        return -1

    mid = int((left + right) / 2)
    if data[mid] == item:
        return mid
    elif data[mid] < item:
        return bin_search(data, item, mid+1, right)
    else:
        return bin_search(data, item, left, mid-1)
