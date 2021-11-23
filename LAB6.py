#Lab #6
#Due Date: 03/22/2020, 11:59PM 
########################################
#                                      
# Name:
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        return ("Node({})".format(self.value)) 

    __repr__ = __str__


class BinarySearchTree:
    '''
        >>> x=BinarySearchTree()
        >>> x.isEmpty()
        True
        >>> x.insert(x.root,9)
        >>> x.insert(x.root,4)
        >>> x.insert(x.root,11)
        >>> x.insert(x.root,2)
        >>> x.insert(x.root,5)
        >>> x.insert(x.root,10)
        >>> x.insert(x.root,9.5)
        >>> x.insert(x.root,7)
        >>> x.getMin
        2
        >>> x.getHeight(x.root)
        3
        >>> x.getHeight(x.root.left.right)
        1
        >>> x.getHeight(x.root.right)
        2
        >>> x.isEmpty()
        False
    '''
    def __init__(self):
        self.root = None

    def insert(self, node, value):
        if(node==None):
            self.root = Node(value)
        else:
            if(value<node.value):
                if(node.left==None):
                    node.left = Node(value)
                else:
                    self.insert(node.left, value)
            else:
                if(node.right==None):
                    node.right = Node(value)
                else:
                    self.insert(node.right, value)


    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.root is None


    @property
    def getMin(self):
        # YOUR CODE STARTS HERE 
        x = self.root
        if x is None:
            return None
        while x.left is not None:
            x=x.left
        return x.value


    def getHeight(self, node):
        # YOUR CODE STARTS HERE
        if node is None:
            return -1
        lef=self.getHeight(node.left)
        rig=self.getHeight(node.right)
        return 1+max(lef,rig)
        


