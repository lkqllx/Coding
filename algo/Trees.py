class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        print("Adding " + child_node.value)
        self.children.append(child_node)

    def remove_child(self, child_node):
        print("Removing " + child_node.value + " from " + self.value)
        self.children = [child for child in self.children
                         if child is not child_node]

    def traverse(self):

        if not self.children:
            print(self.value)
        else:
            print(self.value)
            for child in self.children:
                child.traverse()


root = TreeNode("CEO")
first_child = TreeNode("Vice-President1")
second_child = TreeNode("Vice-President2")
third_child = TreeNode("Head of Marketing3")
fourth_child = TreeNode("Head of Marketing4")
fifth_child = TreeNode("Head of Marketing5")

root.add_child(first_child)
root.add_child(second_child)
first_child.add_child(third_child)
first_child.add_child(fourth_child)
third_child.add_child(fifth_child)

root.traverse()
