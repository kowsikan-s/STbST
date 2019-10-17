class Node:
    def __init__(self, value = None, left = None, right = None):
        self.__value = value
        self.__left = left
        self.__right = right

    def get_value(self):
        return self.__value

    def get_left(self):
        return self.__left

    def get_right(self):
        return self.__right

    def set_value(self, value = None):
        self.__value = value

    def set_left(self, left = None):
        self.__left = left

    def set_right(self, right = None):
        self.__right = right