#invert binary tree

def invertbinary tree(self,root: treenode) -> treednode:
  def dfs(node):
    if i not node:
      return

    dfs(node.left)
    dfs(node.right)

    node.left,node.right=node.right,node.left

    dfs(root)
    return(root)
  
  
