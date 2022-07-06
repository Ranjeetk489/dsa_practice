# node depth
# O(n) time | O(h) space
def nodeDepths(root, depth = 0):
    #base case
    if root is none: return 0
    return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)