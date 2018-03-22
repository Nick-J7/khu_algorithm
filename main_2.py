import random

from company import Company
from bin_search import bin_search
from merge_sort import merge_sort
from quick_sort import quick_sort


def test_bin_serach():
    num_data = 10
    data = []
    for i in range(num_data):
        data.append(Company(i))

    for i in range(len(data)):
        print(data[i].money, end=' ')
    print()

    item = Company(money=2)
    location = bin_search(data, item, 0, len(data)-1)
    print("item : {item.money}\n"
          "location : {location}".format(item=item, location=location))


def test_merge_sort():
    num_data = 10
    data = []
    for i in range(num_data):
        data.append(Company(i))
    random.shuffle(data)

    print("Original data:")
    for i in range(len(data)):
        print(data[i].money, end=' ')
    print()

    memory = [-1] * len(data)
    merge_sort(data, 0, len(data)-1, memory)

    print("Original data:")
    for i in range(len(data)):
        print(data[i].money, end=' ')
    print()


def test_quick_sort():
    num_data = 10
    data = []
    for i in range(num_data):
        data.append(Company(i))
    random.shuffle(data)

    print("Original data:")
    for i in range(len(data)):
        print(data[i].money, end=' ')
    print()

    quick_sort(data, 0, len(data)-1)

    print("Original data:")
    for i in range(len(data)):
        print(data[i].money, end=' ')
    print()

if __name__ == '__main__':
    #test_bin_serach()
    #test_merge_sort()
    test_quick_sort()
