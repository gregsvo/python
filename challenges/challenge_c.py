"""
1.  Create a class that can be used to represent the nodes of a binary tree, 
and then populate a binary tree with the nodes below. (Don't worry about 
writing an insertion algorithm, since the nodes are already mapped out for you.)

2.  Write a search algorithm that, when given an integer, will return that integer's 
depth in the tree. For example, searching for 9 will return 2, while searching for 
14 will return 0. If the provided integer doesn't exist in the tree, return –1.

3.  Search for the integers 0 through 50, and output a file binary_tree_results.txt 
with the results in the following format:

0:-1
1:3
2:2
4:-1
5:3
6:1

"""

class LinkedListItem(object):
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value


node_1 = LinkedListItem(left=None, right=None, value=1)
node_5 = LinkedListItem(left=None, right=None, value=5)
node_17 = LinkedListItem(left=None, right=None, value=17)
node_23 = LinkedListItem(left=None, right=None, value=23)
node_28 = LinkedListItem(left=None, right=None, value=28)
node_38 = LinkedListItem(left=None, right=None, value=38)
node_33 = LinkedListItem(left=node_28, right=node_38, value=33)
node_19 = LinkedListItem(left=node_17, right=node_23, value=19)
node_25 = LinkedListItem(left=node_19, right=node_33, value=25)
node_2 = LinkedListItem(left=node_1, right=node_5, value=2)
node_12 = LinkedListItem(left=None, right=None, value=12)
node_9 = LinkedListItem(left=None, right=node_12, value=9)
node_6 = LinkedListItem(left=node_2, right=node_9, value=6)
node_14 = LinkedListItem(left=node_6, right=node_25, value=14)

search_num = None


def search_list():
    try:
        binary_tree_results_file = open("binary_tree_results.txt", "w+")
        for search_num in range(0, 51):
            binary_tree_results_file.write("{}:{}\n".format(search_num, traverse(search_num)))
    finally:
        binary_tree_results_file.close()


def traverse(search_num=search_num, current_level=0, node=node_14):
    if search_num == node.value:
        return current_level
    else:
        if not node.left and not node.right:
            return -1
        else:
            if search_num < node.value:
                if node.left:
                    current_level += 1
                    next_node = node.left
                else:
                    return -1
            else:
                if node.right:
                    current_level += 1
                    next_node = node.right
                else:
                    return -1
            return traverse(search_num=search_num, current_level=current_level, node=next_node)


if __name__ == "__main__":
    search_list()
