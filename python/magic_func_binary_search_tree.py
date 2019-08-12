class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST():
    def __init__(self, root):
        self.root = Node(root)
        self.print_val = []

    def insert(self, new_val):
        self.find_insert_loc(self.root, new_val)

    def find_insert_loc(self, start, new_val):
        if start:
            if start.value > new_val:
                # go left
                if not start.left:
                    start.left = Node(new_val)
                elif start.left.value < new_val:
                    node = Node(new_val)
                    node.left = start.left
                    start.left = node
                else:
                    self.find_insert_loc(start.left, new_val)
            elif start.value < new_val:
                # go right
                if not start.right:
                    start.right = Node(new_val)
                elif start.right.value > new_val:
                    node = Node(new_val)
                    node.right = start.right
                    start.right = node
                else:
                    self.find_insert_loc(start.right, new_val)

    def search(self, find_val):
        return self.search_aux(self.root, find_val)

    def search_aux(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            return self.search_aux(start.left, find_val) if start.value > find_val else \
                self.search_aux(start.right, find_val)
        return False

    # def __repr__(self):
    #     self.print_aux(self.root)
    #     return '-'.join(self.print_val)

    def __str__(self):
        self.print_aux(self.root)
        return '-'.join(self.print_val)

    def print_aux(self, start):
        if start:
            self.print_val.append(str(start.value))
            self.print_aux(start.left)
            self.print_aux(start.right)

    def __setattr__(self, key, value):
        if not isinstance(value, (Node, list)):
            self.__dict__[key] = value.upper()
        else:
            self.__dict__[key] = value

    def __getattr__(self, item):
        """Will only be triggered when item not in the attributes list"""
        print('Triggered')
        return self.__dict__[item]

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree)
# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))