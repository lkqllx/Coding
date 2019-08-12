from collections import deque

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        self.remains = deque()
        self.match = False
        self.print_val = []

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        self.match = False
        self.preorder_search(self.root, find_val)
        return self.match

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        self.preorder_print(self.root)
        return '-'.join(self.print_val)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        if start.value == find_val:
            """结束条件"""
            self.match = True

        if start.left:
            """先比较左叶，如果右叶不为空值，将右叶加入queue"""
            if start.right:
                self.remains.append(start.right)
            self.preorder_search(start.left, find_val)

        elif start.right:
            """如果左叶为空，搜索右叶"""
            self.preorder_search(start.right, find_val)

        if self.remains:
            """搜索之前剩下的node"""
            self.preorder_search(self.remains.pop(), find_val)

    def preorder_print(self, start):
        """Helper method - use this to create a
        recursive print solution."""
        self.print_val.append(str(start.value))

        if start.left:
            if start.right:
                self.remains.append(start.right)
            self.preorder_print(start.left)
        elif start.right:
            self.preorder_print(start.right)

        if self.remains:
            self.preorder_print(self.remains.pop())

class BinaryTree2(object):
    """Better Way"""
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                """Key is the "or" between left and right"""
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

# Set up tree
tree = BinaryTree2(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())