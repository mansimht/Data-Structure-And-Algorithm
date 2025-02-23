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


def preorder(root):
  if not root:
    return None
  print(root.data)
  preorder(root.leftChild)     #O(n/2)
  preorder(root.rightChild)     #O(n/2)

preorder(newBT)

def InOrder(root):
  if not root:
    return None
  InOrder(root.leftChild)
  print(root.data)
  InOrder(root.rightChild)

InOrder(newBT)

def postorder(root):
  if not root:
    return None
  postorder(root.leftChild)
  postorder(root.rightChild)
  print(root.data)

postorder(newBT)