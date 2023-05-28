from node import Node

class Subtree_Balancer_Split:
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

    def balance_subtree_using_split_and_arrange(self, root):
        if root is None:
            return None

        sorted_list = self.__create_list(root)
        #print(sorted_list)

        return self.__convert_sorted_array_to_BST(sorted_list)

class Subtree_Balancer_DDL_BST(Subtree_Balancer_Split):
    def count_nodes(self, node):
        count = 0
        while node:
            node = node.get_right()
            count = count + 1
        return count

    def convert_sorted_DLL_to_balanced_BST(self, head, count):
        if count <= 0:
            return None, head

        left_subtree, head = self.convert_sorted_DLL_to_balanced_BST(head, count // 2)

        root = head

        root.set_left(left_subtree)

        head = head.get_right()

        right_subtree, head = self.convert_sorted_DLL_to_balanced_BST(head, count - (count // 2 + 1))
        root.set_right(right_subtree)

        return root, head

    def BT_to_DLL(self, root):
        if root is None:
            return root

        if root.get_left():
            left_t = self.BT_to_DLL(root.get_left())

            while left_t.get_right():
                left_t = left_t.get_right()

            left_t.set_right(root)
            root.set_left(left_t)

        if root.get_right():
            right_t = self.BT_to_DLL(root.get_right())

            while right_t.get_left():
                right_t = right_t.get_left()

            right_t.set_left(root)

            root.set_right(right_t)

        return root

    def driver_BT_to_DLL(self, root):
        if root is None:
            return root

        root = self.BT_to_DLL(root)

        while root.get_left():
            root = root.get_left()

        return root

    def balance_subtree(self, root):
        head = self.driver_BT_to_DLL(root)
        new_root, _ = self.convert_sorted_DLL_to_balanced_BST(head, self.count_nodes(head))
        return new_root
