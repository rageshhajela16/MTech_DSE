"""
Data Structures and Algorithms Design
Assignment 1 – PS1 - What tree is this?

Group 323. Members are:
1. Ragesh Hajela (ID No. 2021SC04877 and Email ID: 2021SC04877@wilp.bits-pilani.ac.in)
2. Thakare Kedar Satishrao (ID No. 2021SC04878 and Email ID: 2021SC04878@wilp.bits-pilani.ac.in)
3. D V S Rama Krishna (ID No. 2021SC04879 and Email ID: 2021SC04879@wilp.bits-pilani.ac.in)

Problem Statement:
The input will be the breadth-first search of the tree in a single line
Breadth-first search is the order where you explore each level, left to right. If a child for some
node is not present, it is marked as None. There will always be only one valid tree/solution.

Requirements:
1. Read the input from a file(inputPS1.txt), where each line is a space-separated breadth-first
search of the tree nodes.
2. You will output your answers to a file (outputPS1.txt) for each line.
3. Perform analysis for the features above and give the running time in terms of input size: n (nodes)
4. Implement the above problem statement using Python 3.7.

For example:
Given binary tree: 1,None, 2, 3, 4
    1
  /  \
None  2
    /  \
   3    4
return its boundary traversal as: 1, 3, 4, 2
"""

from typing import List

# List to hold final boundary traversal output
tree_output = []


# Tree Node Data structure
class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def get_leaves(root) -> None:
    """
    A simple function to find leaf nodes of a Binary Tree
    :param root: TreeNode structure representing all tree nodes
    :return: only appends output, nothing to return
    """
    if root:
        get_leaves(root.left)
        # append in final output if it is a leaf node
        if root.left is None and root.right is None:
            tree_output.append(root.data)
        get_leaves(root.right)


def get_left_boundary_nodes(root) -> None:
    """
    A function to find all left boundary nodes in top-down manner, except leaf node.
    :param root: TreeNode structure representing all tree nodes
    :return: only appends output, nothing to return
    """
    if root:
        if root.left:
            # to ensure top down order, append the node
            # before calling itself for left subtree
            tree_output.append(root.data)
            get_left_boundary_nodes(root.left)

        elif root.right:
            tree_output.append(root.data)
            get_left_boundary_nodes(root.right)


def get_right_boundary_nodes(root):
    """
    A function to find all right boundary nodes in bottom up manner, except a leaf node
    :param root: TreeNode structure representing all tree nodes
    :return: only appends output, nothing to return
    """
    if root:
        if root.right:
            # to ensure bottom up order,
            # first call for right subtree, then append the node
            get_right_boundary_nodes(root.right)
            tree_output.append(root.data)

        elif root.left:
            get_right_boundary_nodes(root.left)
            tree_output.append(root.data)


def traverse_boundary(root: TreeNode) -> None:
    """
    A function to perform boundary traversal of a given binary tree
    :param root: TreeNode structure representing all tree nodes
    :return: only appends output, nothing to return
    """
    if root:
        tree_output.append(root.data)

        # traverse the left boundary in top-down manner
        get_left_boundary_nodes(root.left)

        # read all leaf nodes
        get_leaves(root.left)
        get_leaves(root.right)

        # traverse the right boundary in bottom-up manner
        get_right_boundary_nodes(root.right)


def create_binary_tree(tree_nodes_list: List) -> TreeNode:
    """
    A function to create a binary tree
    :param tree_nodes_list: input nodes as either int or NoneType
    :return: created binary tree node data structure
    """
    values = iter(tree_nodes_list)
    root = TreeNode(next(values))
    nodes_to_fill = [root]
    try:
        while True:
            next_node = nodes_to_fill.pop(0)
            new_left = next(values)
            if new_left is not None:
                next_node.left = TreeNode(new_left)
                nodes_to_fill.append(next_node.left)
            new_right = next(values)
            if new_right is not None:
                next_node.right = TreeNode(new_right)
                nodes_to_fill.append(next_node.right)
    except StopIteration:
        return root


def reset_tree_output() -> None:
    """
    A function to reset final list output
    :return: None
    """
    global tree_output
    tree_output = []


def analyze_tree(nodes_str: str):
    """
    A master function to analyze the tree and find boundary traversal output
    :param nodes_str: input all nodes as string
    :return: output all boundary traversed nodes as string
    """
    try:
        nodes_list = [None if el == 'None' else int(el) for el in nodes_str.split()]
    except ValueError:
        print('Error: Problem encountered with input sequence')
        return
    binary_tree: TreeNode = create_binary_tree(nodes_list)
    traverse_boundary(binary_tree)
    str_output = [str(item) for item in tree_output]
    reset_tree_output()
    return ' '.join(str_output)


def main(input_lines) -> None:
    """
    Main function to wrap up execution processing
    :input_lines: all lines from sample input file
    :return: None
    """
    # Remove newline characters read from input samples
    samples = [el.replace('\n', '') for el in input_lines]

    count = 1
    output_to_write = []

    # Iterate through all input samples
    for sample in samples:
        # print(f'Processing sample: {count}')
        # print(f'Input sequence of BFS tree nodes: {sample}')
        traversal_output = analyze_tree(sample)
        output_to_write.append(traversal_output)
        # print(f'Output sequence of boundary traversal: {traversal_output} \n')
        count += 1

    # Write the output file
    out_file = 'outputPS1.txt'
    try:
        with open(out_file, 'w') as f:
            for out in output_to_write:
                f.write(out + '\n')
        # print(f'Congratulations!\nOutput successfully written in {out_file}')
    except TypeError:
        print('Error: Problem encountered with input sequence')


if __name__ == "__main__":
    # Read the input file
    with open('inputPS1.txt') as f:
        lines: List = f.readlines()

    if len(lines) == 0:
        # handle error for empty input file
        print('Input file is empty')
    else:
        main(lines)
