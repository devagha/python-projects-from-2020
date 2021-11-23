#Lab #4
#Due Date: 03/06/2020, 11:59PM 
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
                        
                          
class SortedLinkedList:
    '''
        >>> x=SortedLinkedList()
        >>> x.pop()
        >>> x.add(8.76)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(1)
        >>> x.add(5)
        >>> x.add(3)
        >>> x.pop()
        8.76
        >>> x.add(-7.5)
        >>> x.add(4)
        >>> x.add(9.78)
        >>> x.add(4)
        >>> x
        Head:Node(-7.5)
        Tail:Node(9.78)
        List:-7.5 1 1 1 3 4 4 5 9.78
    '''

    def __init__(self):   # You are not allowed to modify the constructor
        self.head=None
        self.tail=None
        self.count=0

    def __str__(self):   # You are not allowed to modify this method
        temp=self.head
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out=' '.join(out) 
        return ('Head:{}\nTail:{}\nList:{}'.format(self.head,self.tail,out))

    __repr__=__str__


    def isEmpty(self):
        # --- YOUR CODE STARTS HERE
        return self.head == None
    def __len__(self):
        # --- YOUR CODE STARTS HERE
        return self.count
                
    def add(self, value):
        # --- YOUR CODE STARTS HERE
        if self.isEmpty():
            self.head = Node(value)
            self.tail = self.head
            self.count += 1
        elif self.head.value > value:
            node = Node(value)
            node.next = self.head
            self.head = node
            self.count += 1
        else:
            node = Node(value)
            temp = self.head

            while (temp.next):
                if temp.next.value > value:
                    node.next = temp.next
                    temp.next = node
                    self.count +=1
                    return
                temp = temp.next

            temp.next = node
            self.tail = node
            self.count += 1


    def pop(self):
        # --- YOUR CODE STARTS HERE
        if not self.isEmpty():

            value = self.tail.value
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = None
                self.tail = temp
            self.count -= 1
            return value


    # -- If you are attempting the extra credit, uncomment the method definition below

    #def replicate(self):
        # --- YOUR CODE STARTS HERE



