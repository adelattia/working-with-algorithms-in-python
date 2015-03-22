from binary_search_tree import BinaryTree


def balanced_tree(ordered):
    """Create balanced binary tree from ordered collection"""
    bt = BinaryTree()

    add_range(bt, ordered, 0, len(ordered)-1)

    return bt


def add_range(bt, ordered, low, high):
    """Add range to the bt in a way that Bt remains balanced"""

    if low <= high:
        mid = (low+high)//2

        bt.add(ordered[mid])
        add_range(bt, ordered, low, mid-1)
        add_range(bt, ordered, mid+1, high)


x = list(range(10))
print(x)

bt = balanced_tree(x)
print(bt.root.value)
print(bt.root.left.value)
print(bt.root.right.value)
print(bt.root.left.left.value)
print(bt.root.left.right.value)