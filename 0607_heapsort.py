import pdb


class Heap:
    """

    Args:
        data (list): list of int
    """
    def __init__(self, data):
        self.data = list(data)
        self.num_of_data = len(data)
        self.tree = [0]
        #self.make_heap()
        self.make_heap_second()

    def heap_sort(self):
        tmp_tree = list(self.tree)
        sorted_list = []
        for i in range(self.num_of_data):
            cur_max_value = self.remove_element(tmp_tree)
            sorted_list.append(cur_max_value)
        return sorted_list

    def make_heap(self):
        for value in self.data:
            self.add_element(value)

    def make_heap_second(self):
        for value in self.data:
            self.tree.append(value)
        for i in range(len(self.tree), 0, -1):
            self.sift_down_for_make_heap(i)

    def add_element(self, value):
        self.tree.append(value)
        self.sift_up()

    def remove_element(self, tree):
        result = tree[1]
        tree[1] = tree[-1]
        del tree[-1]
        self.sift_down(tree)
        return result

    def sift_up(self):
        child_index = len(self.tree) - 1
        parent_index = int(child_index / 2)
        child_value = self.tree[child_index]
        parent_value = self.tree[parent_index]
        while child_value > parent_value and parent_index != 0:
            self.tree[parent_index] = child_value
            self.tree[child_index] = parent_value

            child_index = parent_index
            parent_index = int(child_index / 2)
            child_value = self.tree[child_index]
            parent_value = self.tree[parent_index]

    def sift_down(self, tree):
        last_index = len(tree) - 1

        parent_index = 1 
        left_child_index = 2 * parent_index
        right_child_index = 2 * parent_index + 1
        if left_child_index > last_index:
            return

        if right_child_index <= last_index:
            parent_value = tree[parent_index]
            left_child_value = tree[left_child_index]
            right_child_value = tree[right_child_index]
            max_child_value = max(left_child_value, right_child_value)
        else:
            parent_value = tree[parent_index]
            left_child_value = tree[left_child_index]
            max_child_value = left_child_value

        while parent_value < max_child_value:
            if max_child_value == left_child_value:
                tree[parent_index] = left_child_value
                tree[left_child_index] = parent_value
                parent_index = left_child_index
            else:
                tree[parent_index] = right_child_value
                tree[right_child_index] = parent_value
                parent_index = right_child_index

            left_child_index = 2 * parent_index
            right_child_index = 2 * parent_index + 1

            if left_child_index > last_index:
                break

            if right_child_index <= last_index:
                parent_value = tree[parent_index]
                left_child_value = tree[left_child_index]
                right_child_value = tree[right_child_index]
                max_child_value = max(left_child_value, right_child_value)
            else:
                parent_value = tree[parent_index]
                left_child_value = tree[left_child_index]
                max_child_value = left_child_value

    def sift_down_for_make_heap(self, root):

        last_index = len(self.tree) - 1

        parent_index = root 
        left_child_index = 2 * parent_index
        right_child_index = 2 * parent_index + 1
        if left_child_index > last_index:
            return

        if right_child_index <= last_index:
            parent_value = self.tree[parent_index]
            left_child_value = self.tree[left_child_index]
            right_child_value = self.tree[right_child_index]
            max_child_value = max(left_child_value, right_child_value)
        else:
            parent_value = self.tree[parent_index]
            left_child_value = self.tree[left_child_index]
            max_child_value = left_child_value

        while parent_value < max_child_value:
            if max_child_value == left_child_value:
                self.tree[parent_index] = left_child_value
                self.tree[left_child_index] = parent_value
                parent_index = left_child_index
            else:
                self.tree[parent_index] = right_child_value
                self.tree[right_child_index] = parent_value
                parent_index = right_child_index

            left_child_index = 2 * parent_index
            right_child_index = 2 * parent_index + 1

            if left_child_index > last_index:
                break

            if right_child_index <= last_index:
                parent_value = self.tree[parent_index]
                left_child_value = self.tree[left_child_index]
                right_child_value = self.tree[right_child_index]
                max_child_value = max(left_child_value, right_child_value)
            else:
                parent_value = self.tree[parent_index]
                left_child_value = self.tree[left_child_index]
                max_child_value = left_child_value

init_list = [11, 14, 2, 7, 6, 3, 9, 5]
heap = Heap(init_list)
print(heap.tree)
# print(heap.remove_element(heap.tree))
# print(heap.tree)
sorted_list = heap.heap_sort()
print(sorted_list)

