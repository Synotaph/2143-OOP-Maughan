"""
Program:
--------
    Homework 1

Description:
------------
    This program adds and divides fractions. I added the ability 
    to handle mixed numbers into the class definition and print
    functions.

Name: Zachary Maughan
Date: 5 Feb 2016
"""

class fraction(object):
    def __init__(self,n=None,d=None,w=None,m=False):
        self.numerator = n
        self.denominator = d
        self.whole = w
        self.mixed = m

    def __str__(self):
        if self.mixed == True:
            return "%d %d/%d" % (self.whole , self.numerator , self.denominator)
        else:
            return "%d/%d" % (self.numerator , self.denominator)

    """
    Description:
    ------------
        This function adds two fractions together, and handles reducing fractions into mixed numbers.

    Params:
    -------
        rhs - (fraction) The right hand side of the operation

    Returns:
    --------
        (fraction) - result of operation, either as a fraction or mixed number
    """


    def __add__(self,rhs):
        a = self.denominator
        b = rhs.denominator
        x = (self.numerator * b) + (rhs.numerator * a)
        y = self.denominator * b
        if x > y:
            w = x / y
            x -= y
            return fraction(x,y,w,True)
        else:
            return fraction(x,y)
        
    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d
        
    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)
    


a = fraction(1,2)
b = fraction(4,5)
c = a + b
print(c)