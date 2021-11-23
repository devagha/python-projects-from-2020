#Lab #5
#Due Date: 03/22/2020, 11:59PM 
########################################
#                                      
# Name:devan ghai
# Collaboration Statement:             
#
########################################

class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 

    __repr__ = __str__
                        
                          
class Queue:
    '''
        >>> x=Queue()
        >>> x.isEmpty()
        True
        >>> x.dequeue()
        >>> x.enqueue(1)
        >>> x.enqueue(2)
        >>> x.enqueue(3)
        >>> x.dequeue()
        1
        >>> len(x)
        2
    '''
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out)
        return f'Head:{self.head}\nTail:{self.tail}\nQueue:{out}'

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.count==0:
            return True
        return False

    def enqueue(self, value):
        # YOUR CODE STARTS HERE
        node_z=Node(value)
        if self.count==0:
            self.head=node_z
            self.tail=node_z
        else:
            self.tail.next=node_z
            self.tail=node_z
        self.count+=1


    def dequeue(self):
        # YOUR CODE STARTS HERE
        if self.count == 0:
            return 'empty queue'
        else:
            r_e = self.head.value
            self.head=self.head.next
            return r_e
                  
    def __len__(self):
        # YOUR CODE STARTS HERE
        return self.count

