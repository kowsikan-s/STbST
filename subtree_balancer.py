from node import Node

class Subtree_Balancer:
    def __init__(self):
        pass

    def __create_list(self, node):
        if node is None:
            return []
        return self.__create_list(node.get_left()) + [node.get_value()] + self.__create_list(node.get_right())

    def __convert_sorted_array_to_BST(self, arr):
        if not arr:
            return None

        mid = int((len(arr)) / 2)

        root = Node(arr[mid])
        root.set_left(self.__convert_sorted_array_to_BST(arr[:mid]))
        root.set_right(self.__convert_sorted_array_to_BST(arr[mid + 1:]))

        return root

    def balance_subtree(self, root):
        if root is None:
            return None

        sorted_list = self.__create_list(root)
        #print(sorted_list)

        return self.__convert_sorted_array_to_BST(sorted_list)

