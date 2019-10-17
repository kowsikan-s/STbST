from splay_tree import Splay_Tree

insert_list = [1,2, 0,3,4,5,6, 5,12,13,14,15,-1,-2,-3]
splay_tree = Splay_Tree()

for value in insert_list:
    splay_tree.insert(value)
    print("Current Root is ", splay_tree.get_root().get_value())

print(splay_tree.find(1))
print(splay_tree.find(2))
#splay_tree.pre_order(splay_tree.get_root())
print(splay_tree.find(4))

print("Pre order")
splay_tree.pre_order(splay_tree.get_root())

#splay_tree.remove(2)
print("After deleting, root is : ", splay_tree.get_root().get_value())

print("Pre order")
splay_tree.pre_order(splay_tree.get_root())

#######################################################################################################