from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def max_depth(root: Optional[TreeNode]) -> int:
    """
    Calculate the maximum depth of a binary tree.
    Depth is the number of nodes along the longest path from root to leaf.
    """
    # Base case: empty tree has depth 0
    if root is None:
        return 0
    
    # Recursive case: depth = 1 + max(left_depth, right_depth)
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    return 1 + max(left_depth, right_depth)

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree.
    Leverages BST property: left < root < right
    """
    # If both nodes are less than root, LCA is in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # If both nodes are greater than root, LCA is in right subtree
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # Otherwise, we've found the split point - root is the LCA
    # (either nodes are on different sides, or one is the root itself)
    else:
        return root