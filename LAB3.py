#Lab #3
#Due Date: 02/21/2020, 11:59PM 
########################################
#                                      
# Name:devan ghai
# Collaboration Statement:             
#
########################################

'''
    REMINDER: All functions should not contain any for or while loops, or global variables. 
    Use recursion otherwise, no credit will be given
'''

def thirtyTwos(n,o):
    '''
        >>> thirtyTwos(432601)
        1
        >>> thirtyTwos(132432601)
        2
        >>> thirtyTwos(78)
        0
    '''
    ## YOUR CODE STARTS HERE
    if n<=0:
        return o
    else:
        if (n%100==32):
            o+=1
        return thirtyTwos(n/10,o)




def flat(aList):
    '''
        >>> x = [3, [[5, 2]], 6, [4]]
        >>> flat(x)
        [3, 5, 2, 6, 4]
        >>> x
        [3, [[5, 2]], 6, [4]]
        >>> flat([1, 2, 3])
        [1, 2, 3]
        >>> flat([1, [], 3])
        [1, 3]
    '''
    ## YOUR CODE STARTS HERE
    if aList==[]:
        return aList
    if isinstance(aList[0], list):
        return flat(aList[0]) + flat(aList[1:])
    return aList[:1] + flat(aList[1:])
    
        

############# DO NOT modify the triangle(n) function in any way! 
def triangle(n):
    return recursiveTriangle(n, n)
###################
    
def recursiveTriangle(k, n):
    '''
        >>> recursiveTriangle(2,4)
        '  **\\n   *'
        >>> print(recursiveTriangle(2,4))
          **
           *
        >>> triangle(4)
        '****\\n ***\\n  **\\n   *'
        >>> print(triangle(4))
        ****
         ***
          **
           *
    '''
    ## YOUR CODE STARTS HERE
    if k==1:
        return ''*(n-k)+'*'*k
    else:
        return ''*(n-k)+'*'*k+'\n'+recursiveTriangle(k-1,n)



def isPrime(num, i=2):
    '''
        >>> isPrime(5)
        True
        >>> isPrime(1)
        False
        >>> isPrime(0)
        False
        >>> isPrime(85)
        False
        >>> isPrime(1019)
        True
        >>> isPrime(2654)
        False
    '''
    ## YOUR CODE STARTS HERE
    if num<=1:
        return False
    if i>(num**.5):
        return True
    if num%i==0:
        return False
    return isPrime(num,i+1)



