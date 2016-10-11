#!/usr/bin/env python3

import random
import uuid

from graphviz import Digraph

class BinaryTreeNode:

  def __init__(self, value):
      self.value = value
      self.left  = None
      self.right = None

  def insert_left(self, value):
      self.left = BinaryTreeNode(value)
      return self.left

  def insert_right(self, value):
      self.right = BinaryTreeNode(value)
      return self.right

def is_super_balanced(node):
    max_depth = get_max_depth(node)
    min_depth = get_min_depth(node)

    return max_depth <= (min_depth + 1)

def get_max_depth(node):
    if not isinstance(node, BinaryTreeNode):
        return 1
    return 1 + max(get_max_depth(node.left), get_max_depth(node.right))

def get_min_depth(node):
    if not isinstance(node, BinaryTreeNode):
        return 1
    return 1 + min(get_min_depth(node.left), get_min_depth(node.right))

def is_super_balanced_i(node):
    # Create two lists:
    # depths - contains unique depths of leafs
    # nodes_w_d - contains tree node with depth
    depths = []
    nodes_w_d = []

    nodes_w_d.append([node, 0])

    # This cycle returns false if not superbalanced
    # Does the following:
    # - Take a node from list
    # - If leaf, append depth and check conditions
    # - Else, append to nodes left and right members with depths
    while len(nodes_w_d):
        node_w_d = nodes_w_d.pop()
        node = node_w_d[0]
        depth = node_w_d[1]

        # Check special case, when node have only one child.
        if int(bool(node.left)) + int(bool(node.right)) == 1:
            if depth not in depths:
                depths.append(depth)

        # If leaf
        if not (node.left or node.right):
            # Append only new depth
            if depth not in depths:
                depths.append(depth)
                # Two cases when tree is not superbalances:
                # 1) We have more that 2 uniq lengths in list
                # 2) Difference between them more that 1
                if len(depths) > 2 or \
                   (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
        # Append nodes with depths
        else:
            if node.left:
                nodes_w_d.append([node.left, depth + 1])
            if node.right:
                nodes_w_d.append([node.right, depth + 1])

    # Case with 1 leaf
    if len(depths) == 1 and depths[0] > 1:
        return False

    # SuperBalanced
    return True

def inorder_tree_walk(node):
    if node.left:
        inorder_tree_walk(node.left)
    print(node.value)
    if node.right:
        inorder_tree_walk(node.right)

def rand():
    return random.randint(1, 100)

def create_children(node):
    if rand() > 50:
        create_children(node.insert_left(rand()))

    if rand() > 50:
        create_children(node.insert_right(rand()))

def visualize_children(node, graph, parent_id):
    if node.left:
        lchild_id = str(uuid.uuid4())
        graph.node(lchild_id, str(node.left.value))
        graph.edge(parent_id, lchild_id)
        visualize_children(node.left, graph, lchild_id)
    if node.right:
        rchild_id = str(uuid.uuid4())
        graph.node(rchild_id, str(node.right.value))
        graph.edge(parent_id, rchild_id)
        visualize_children(node.right, graph, rchild_id)

def visualize_tree(root):
    graph = Digraph()
    root_id = str(uuid.uuid4())
    graph.node(root_id, str(root.value))
    visualize_children(root, graph, root_id)
    graph.render('test.gv')

def create_binary_tree():
    root = BinaryTreeNode(rand())
    create_children(root)
    return root


if __name__ == '__main__':
    # Generate random binary tree
    bt = create_binary_tree()

    # Check recursively
    recursive_result = is_super_balanced(bt)
    print("Recursive: %s" % recursive_result)

    # Check iteratively
    iterative_result = is_super_balanced_i(bt)
    print("Iterative: %s" % iterative_result)

    # Generate dot test.gv and test.gv.pdf
    #visualize_tree(bt)

    # Walk tree
    #inorder_tree_walk(bt)
