from node import Node
from subtree_balancer import Subtree_Balancer

class Splay_Tree:
    def __init__(self, root = None, header = Node(None)):
        self.__root = root
        self.__header = header

    def get_root(self):
        return self.__root

    def get_header(self):
        return self.__header

    def set_root(self, root = None):
        self.__root = root

    def set_header(self, header = None):
        self.__header = header

    def find(self, value):
        try:
            if self.get_root() is None:
                return None

            self.__splay(value)
            if self.get_root().get_value() != value:
                return None

            self.__balance_subtree()

            return self.get_root().get_value()

        except Exception as issue:
            print("Issue while finding operation : ", issue)

    def insert(self, value):
        try:
            if self.get_root() is None:
                # print("Root is None, Inserting new root : ", value)
                self.set_root(Node(value))
                return

            self.__splay(value)

            root_value = self.get_root().get_value()
            if value == root_value:
                # print("Value already available, So not inserting")
                return

            node = Node(value)
            if value < root_value:
                # print("Value less than root value")
                node.set_left(self.get_root().get_left())
                node.set_right(self.get_root())
                self.get_root().set_left()
            else:
                # print("Value greater than root value")
                node.set_right(self.get_root().get_right())
                node.set_left(self.get_root())
                self.get_root().set_right()

            self.set_root(node)
            # print("Inserted : ", value)

            self.__balance_subtree()

            return

        except Exception as issue:
            print("Issue while inserting operation : ", issue)

    def remove(self, value):
        try:
            self.__splay(value)
            if value != self.get_root().get_value():
                return "Value not found"

            if self.get_root().get_left() is None:
                self.set_root(self.get_root().get_right())
            else:
                temp = self.get_root().get_right()
                self.set_root(self.get_root().get_left())
                self.__splay(value)
                self.get_root().set_right(temp)

            self.__balance_subtree()

        except Exception as issue:
            print("Issue while removing operation : ", issue)

    def __balance_subtree(self):
        try:
            subtree_balancer = Subtree_Balancer()
            self.get_root().set_left(subtree_balancer.balance_subtree(self.get_root().get_left()))
            self.get_root().set_right(subtree_balancer.balance_subtree(self.get_root().get_right()))

        except Exception as issue:
            print("Issue while subtree balancing operation : ", issue)

    def __splay(self, value):
        try:
            left = self.get_header()
            right = self.get_header()
            target = self.get_root()

            self.get_header().set_left()
            self.get_header().set_right()

            while True:
                if value < target.get_value():
                    if target.get_left() is None:
                        break

                    if value < target.get_left().get_value():
                        temp = target.get_left()
                        target.set_left(temp.get_right())
                        temp.set_right(target)
                        target = temp

                        if target.get_left() is None:
                            break
                    right.set_left(target)
                    right = target
                    target = target.get_left()

                elif value > target.get_value():
                    if target.get_right() is None:
                        break

                    if value > target.get_right().get_value():
                        temp = target.get_right()
                        target.set_right(temp.get_left())
                        temp.set_left(target)
                        target = temp

                        if target.get_right() is None:
                            break
                    left.set_right(target)
                    left = target
                    target = target.get_right()
                else:
                    break

            left.set_right(target.get_left())
            right.set_left(target.get_right())
            target.set_left(self.get_header().get_right())
            target.set_right(self.get_header().get_left())
            self.set_root(target)
            return

        except Exception as issue:
            print("Issue while splaying operation : ", issue)

    def pre_order(self, node):
        if not node:
            return
        print(node.get_value())
        self.pre_order(node.get_left())
        self.pre_order(node.get_right())