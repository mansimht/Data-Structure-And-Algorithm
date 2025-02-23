#Level order Traverasall using DFS and stack
class TreeNode:
  def __init__(self,data):
    self.data= data
    self.leftChild= None
    self.rightChild= None

newBT= TreeNode("Drinks")
leftChild= TreeNode("Hot")
rightChild= TreeNode('Cold')
leftChild1= TreeNode("Tea")
rightChild1= TreeNode('Frappe')
newBT.leftChild= leftChild
newBT.rightChild= rightChild
newBT.leftChild.leftChild= leftChild1
newBT.rightChild.rightChild= rightChild1

def levelorderdfs(root,level=0,res=None):
  if not root:
    return
  
  if res is None:
        res = []
  
  # Expand res if necessary
  if len(res) <= level:
    res.append([])

  # Append the current node's value
  res[level].append(root.data)

  # Recur for left and right children
  levelorderdfs(root.leftChild, level + 1, res)
  levelorderdfs(root.rightChild, level + 1, res)
  return res

levelorderdfs(newBT)
  
