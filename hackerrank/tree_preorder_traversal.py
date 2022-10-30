# What I learned 
# 1) use stack to return to original node 

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    # Record where you've been 
    # stack to return to  
 
    check = [] 
    stack = []
    stack.append(root)
    while len(stack)!=0:
        targ = stack[-1]
        if targ.info not in check: 
            check.append(targ.info)
        if targ.left != None and targ.left.info not in check: 
            stack.append(targ.left)
            continue 
        elif targ.right != None and targ.right.info not in check: 
            stack.append(targ.right)
            continue 
        targ = stack.pop()
    
    print(' '.join(map(str,check)))
    

