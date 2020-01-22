class Tree:

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"Tree({repr(self.value)})"
    
def insert(tree, value):
    if value < tree.value:
        if tree.left is None:
            tree.left = Tree(value)
        else:
            insert(tree.left, value)
    else:
        if tree.right is None:
            tree.right = Tree(value)
        else:
            insert(tree.right, value)


def construct_bst(nums):
    if not nums:
        return
    
    root = Tree(nums[0])

    for n in nums[1:]:
        insert(root, n)

    return root

