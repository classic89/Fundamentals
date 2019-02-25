class node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def get(self):
        return self.value

    def set(self, value):
        self.value = value

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_children(self):
        children = {
            'left_child': self.left_child,
            'right_child': self.right_child
        }
        return children


# methods needed:
# insert(), find(), delete()
class binary_search_tree:
    def __init__(self):
        self.root = None

    def set_root(self, value):
        self.root = node(value)

    def insert(self, value):
        if(self.root is None):
            self.set_root(value)
        else:
            self.__insert_node(self.root, value)

    def __insert_node(self, current_node, value):
        if(value < current_node.value):
            if(current_node.left_child):
                self.__insert_node(current_node.left_child, value)
            else:
                current_node.left_child = node(value)
        elif(value > current_node.value):
            if(current_node.right_child):
                self.__insert_node(current_node.right_child, value)
            else:
                current_node.right_child = node(value)

    def find(self, value):
        return self.__find_node(self.root, value)

    def __find_node(self, current_node, value):
        if(current_node is None):
            return False
        elif(value == current_node.value):
            return current_node
        elif(value <= current_node.value):
            return self.__find_node(current_node.left_child, value)
        elif(value > current_node.value):
            return self.__find_node(current_node.right_child, value)


bst = binary_search_tree()
bst.set_root(5)
bst.insert(4)
print(bst.find(4).value)

