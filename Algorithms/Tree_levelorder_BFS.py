#Level Order Binary Tree- Breath First Search= go level by level 
from collections import deque
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

def levelorder(root):
  #create list to store the levels
  ans=[]
  if not root:
    return ans

  #create queue for store nodes of level order
  q= deque()

  #Enqueue queue qith root node
  q.append(root)

  #iterate until queue is empty
  while q:
    #get size of queue
    size= len(q)
    #create new level vector
    level=[]
    #iterate through size of number of nodes
    for i in range(size):
      #Get front node of queue
      node= q.popleft()
      #store node value into level vector
      level.append(node.data)

      #enque childnode if exists
      if node.leftChild:
        q.append(node.leftChild)
      if node.rightChild:
        q.append(node.rightChild)
    
    #Store current level into ans
    ans.append(level)
    #Return level order traversal of tree
  return ans

levelorder(newBT)