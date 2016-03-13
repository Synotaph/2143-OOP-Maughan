"""
Program:
--------
    Balanced Binary Tree

Description:
------------
    This program promts the user to specify the number of items that will be placed into a binary search tree.
    the program then populates a list with random values, sorts those values, and then places them into a list
    -based binary search tree.

Name: Zachary Maughan
Date: 10 March 2016
"""
import random
import time

"""
@Class: BalancedSearchTree 
@Usage: 
    tree = BalancedSearchTree()     # creates a tree 
    tree2 = BalancedSearchTree(50)  # creates a tree with 50 items

@Description:
    This class creates a binary search tree, and contains functions to populate itself.
@Params:
    size - (int) This determines the initial size of the tree
@Methods:
    buildTree - Builds the binary search tree from the list given to it.
        usage: buildTree(list)
    insert - Used by buildTree to insert the passed value into the correct place in the tree
        usage: insert(value)
    child - Used by insert to handle organization by left/right child in the tree
        usage: child(value,'r')
    extend - Used by insert to extend the tree if the list is too small
        usage: extend()
    populate - Generates a list with a user-defined number of random values
        usage: populate()
    setup - Used by buildTree to order the list to balance the tree as it is being inserted
        usage: setup(list)
"""
class BalancedSearchTree(object):
    def __init__(self,size=16):
        self.tree = [-1 for x in range(size)]
        self.size = size
        self.root = 1
        self.items = []
    
    def buildTree(self,list):
        """
        @Description:
            This method sorts the list given to it, then it prepares it to be built into a tree, 
            then builds the tree from the list.
        @Params:
            list - (list) The list to be sorted into a tree.
        @Returns:
            none
        """

        list.sort()
        self.setup(list)
        for i in self.items:
            self.insert(i)
    
    def insert(self,val):
        """
        @Description:
            This method inserts values into their proper place in the tree
        @Params:
            val - (int) The value to be placed.
        @Returns:
            none
        """
        # If list (tree) is empty, put value at root
        if self.tree[self.root] == -1:
            self.tree[self.root] = val
        # loop until you find the location to insert
        # even if you have to extend this list
        else:
            i = self.root
            loop = True
            while loop:
                if val > self.tree[i]:
                    i = self.child(i,'r')
                else:
                    i = self.child(i,'l')
                
                if i >= self.size:
                    self.extend()
                
                if self.tree[i] == -1:
                    self.tree[i] = val
                    loop = False
        
    def child(self,i,side):
        """
        @Description:
            This method tests for left or right child, and returns the appropriate place in the 
            list for this value.
        @Params:
            i - (int) The place of the parent in the list.
            side - (str) The marker for "left" or "right"
        @Returns:
            (int) - the place of the child in relation to the parent
        """
        if side == 'l':
            return 2 * i
        elif side == 'r':
            return 2 * i + 1
        else:
            return

    def extend(self):
        """
        @Description:
            This method expands the list that the tree is built in.
        @Params:
            none
        @Returns:
            none
        """
        temp = [-1 for x in range(self.size)]
        self.tree.extend(temp)
        self.size *= 2
        print(len(self.items))

    def populate(self,num):
        """
        @Description:
            This method generates a list and fills that list with a passed-in amount of random values.
        @Params:
            num - (int) The number of values to populate the list with.
        @Returns:
            none
        """
        temp = []
        random.seed(time.time())
        for x in range(size):
            r = random.randint(0,99999)
            if r not in temp:
                temp.append(r)
        self.buildTree(temp)
    
    def setup(self,list):
        """
        @Description:
            This method takes the values in the passed list, and enters them into the 
            main list in the proper order to create a balanced list.
        @Params:
            list - (list) The list of numbers being pulled from.
        @Returns:
            none
        """
        if len(list) == 0:
            return
        else:
            self.items.append(list[len(list)//2])
            self.setup(list[:len(list)//2])
            self.setup(list[len(list)//2+1:])
        

size = int(input('Number to insert: '))
bst = BalancedSearchTree()
bst.populate(size)
print(bst.tree)