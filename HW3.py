#HW3
#Due Date: 03/27/2020, 11:59PM 
########################################
#                                      
# Name:
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
                          

#=============================================== Part I ==============================================

class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE CONSTRUCTOR
        self.top = None
        self.count=0
    
    def __str__(self):
        # YOU ARE NOT ALLOWED TO MODIFY THE THIS METHOD
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))

    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        if self.top == None:
            return True
        else:
            return False
        pass

    def __len__(self): 
        # YOUR CODE STARTS HERE
        return self.count
        pass

    def push(self,value):
        # YOUR CODE STARTS HERE
        newnode=Node(value)
        newnode.next=self.top
        self.top=newnode #new node on top same value as node before
        self.count = self.count+1
        pass

     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() is False:
            value=self.top.value #value of node removed from stack
            self.top=self.top.next 
            self.count-=1
            return value
        pass

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty() is False:
            return self.top.value  #if not empty return top node
        pass


#=============================================== Part II ==============================================

class Calculator:
    def __init__(self):
        self.__expr = None

    @property
    def getExpr(self):
        return self.__expr

    def setExpr(self, new_expr):
        if isinstance(new_expr, str) and len(new_expr.strip())>0:
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None


    def isNumber(self, txt):
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in isNumber")
            return False
        # YOUR CODE STARTS HERE
        if float(txt):
            return True
        else:
            return False
            
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack for expression processing. Follow PEMDAS
            >>> x=Calculator()
            >>> x._getPostfix(' 2 ^        4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1*5+3^2+1+4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('    2 *       5.34        +       3      ^ 2    + 1+4   ')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix(' 2.1 *      5   +   3    ^ 2+ 1  +     4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('(2.5)')
            '2.5'
            >>> x._getPostfix ('((2))')
            '2.0'
            >>> x._getPostfix ('     2 *  ((  5   +   3)    ^ 2+(1  +4))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  (   2 *  ((  5   +   3)    ^ 2+(1  +4)))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('  ((   2 *  ((  5   +   3)    ^ 2+(1  +4))))    ')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4)    ')
            '2.0 5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            # If you are veryfing the expression in calculate before passing to postfix, this cases are not necessary

            >>> x._getPostfix('2 *    5   +   3    ^ -2       +1  +4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix('   2 *  (  5   +   3)    ^ 2+(1  +4    ')
            >>> x._getPostfix('2*(5 +3)^ 2+)1  +4(    ')
        '''
        if not isinstance(txt,str) or len(txt.strip())==0:
            print("Argument error in _getPostfix")
            return None

        postfix_Stack=Stack()
        # YOUR CODE STARTS HERE
        emdas={}
        emdas['^']=4
        emdas['*']=3
        emdas['/']=3
        emdas['+']=2
        emdas['-']=2
        emdas['(']=1
        post=[]
        charlist=txt.split()
        for char in charlist:
            if isinstance(char,int):
                post.append(char)
            elif char is '(':
                postfix_Stack.push(char)
            elif char is ')':
                topchar=postfix_Stack.pop()
                while topchar !='(':
                    post.append(topchar)
                    topchar=postfix_Stack.pop()
            else:
                while (not postfix_Stack.isEmpty()) and (emdas[postfix_Stack.peek()] >= emdas[char]):
                    post.append(postfix_Stack.pop())
                    postfix_Stack.push(char)
        while not postfix_Stack.isEmpty():
            post.append(postfix_Stack.pop())
        return ''.join(post)


    @property
    def calculate(self):
        '''
            Required: calculate must call postfix
                      calculate must create and use a Stack to compute the final result as shown in the video lecture
            >>> x=Calculator()
            >>> x.setExpr('    4  +      3 -2')
            >>> x.calculate
            5.0
            >>> x.setExpr('  2  +3.5')
            >>> x.calculate
            5.5
            >>> x.setExpr('4+3.65-2 /2')
            >>> x.calculate
            6.65
            >>> x.setExpr(' 23 / 12 - 223 +      5.25 * 4    *      3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr('   2   - 3         *4')
            >>> x.calculate
            -10.0
            >>> x.setExpr(' 3 *   (        ( (10 - 2*3)))')
            >>> x.calculate
            12.0
            >>> x.setExpr(' 8 / 4  * (3 - 2.45      * (  4- 2 ^   3)) + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr(' 2   *  ( 4 + 2 *   (5-3^2)+1)+4')
            >>> x.calculate
            -2.0
            >>> x.setExpr('2.5 + 3 * ( 2 +(3.0) *(5^2 - 2*3^(2) ) *(4) ) * ( 2 /8 + 2*( 3 - 1/ 3) ) - 2/ 3^2')
            >>> x.calculate
            1442.7777777777778
            

            # In invalid expressions, you might print an error message, but code must return None, adjust doctest accordingly
            >>> x.setExpr("4++ 3 +2") 
            >>> x.calculate
            >>> x.setExpr("4    3 +2")
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*(2 - 3*2)) ')
            >>> x.calculate
            >>> x.setExpr('(2)*10 - 3*/(2 - 3*2) ')
            >>> x.calculate
            >>> x.setExpr(')2(*10 - 3*(2 - 3*2) ')
            >>> x.calculate
        '''

        if not isinstance(self.__expr,str) or len(self.__expr.strip())==0:
            print("Argument error in calculate")
            return None

        calculator_Stack=Stack()
        # YOUR CODE STARTS HERE
