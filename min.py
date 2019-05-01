import math
import sys


# example case: min of interval
class SegmentTree:
    def __init__(self, data):
        self._data = data

        # initial tree
        tree_length = self._compute_tree_length()
        # - initial value can be arbitrary
        self._tree = [0] * tree_length

        self._built_tree(0, len(self._data) - 1, 0)

    # TODO: update raw data value at index i
    def update(self, i, val):
        pass

    # get result of interval [start, end]
    # , in this case result is "min"
    def query(self, start, end):
        return self._query(start, end, 0, len(self._data) - 1, 0)

    # tree length = 2 * (next power of 2 of data length) - 1
    def _compute_tree_length(self):
        data_length = len(self._data)
        next_power_of_two = int(2 ** math.ceil(math.log(data_length, 2)))
        return 2 * next_power_of_two - 1

    # built segment tree
    # - start, end: index of raw data
    # - position: node position in tree
    def _built_tree(self, start, end, position):
        if start == end:
            # is leaf node:
            # node interval: [start:start]

            # TODO: modify here
            # depends on usage, in "min" case, the value should be min of interval
            self._tree[position] = self._data[start]
        else:
            # is branch node:
            # node interval: [start:end]

            mid = start + (end - start) / 2
            self._built_tree(start, mid, position * 2 + 1)
            self._built_tree(mid + 1, end, position * 2 + 2)

            # TODO: modify here
            # depends on usage, in this case the value in tree is "min"
            self._tree[position] = min(self._tree[position * 2 + 1], self._tree[position * 2 + 2])

    # start, end: queried range of raw data
    # node_start, node_end: raw data range of current node
    # position: position of current node in tree
    def _query(self, start, end, node_start, node_end, position):
        if start <= node_start and end >= node_end:
            # complete overlap
            return self._tree[position]
        elif end < node_start or start > node_end:
            # not overlap

            # TODO: modify here
            # depends on usage, in "min" case, the value should be max int (to reflect that interval is out of range)
            return sys.maxint
        else:
            # partial overlap
            node_mid = node_start + (node_end - node_start) / 2

            res_left = self._query(start, end, node_start, node_mid, position * 2 + 1)
            res_right = self._query(start, end, node_mid + 1, node_end, position * 2 + 2)

            # TODO: modify here
            # depends on usage, in "min" case, the value should be min of left child & right child
            return min(res_left, res_right)


def test(i, j, st):
    print a[i:j + 1], st.query(i, j)


# test
a = [5, 9, 8, 10, 3]
tree = SegmentTree(a)
test(0, 2, tree)
test(2, 4, tree)
test(0, 4, tree)
test(1, 3, tree)
test(0, 3, tree)
test(1, 4, tree)
test(2, 3, tree)
test(3, 4, tree)
test(0, 1, tree)
test(1, 2, tree)
test(0, 0, tree)
test(1, 1, tree)
test(2, 2, tree)
test(3, 3, tree)
test(4, 4, tree)
