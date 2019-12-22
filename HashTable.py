##############################
# Created by Samuelito Perro
# This is a program that implements a HashTable using only lists (and technically sets too)
# Collision Handling done with Separate Chaining using sets
##############################
import sys

#* Implementing feedback.
#! Feedback stuff is on red

class HashTable:
    #! Hard coded size better implemented as a class constant
    T_SIZE = 54
    
    # Initialize the table
    def __init__(self):
        #! Encapsulate the crucial table as a protected property
        self._Table = [None] * HashTable.T_SIZE

    #! Create a _check_value() method to avoid repetitive calls and condition check
    #! Specifically avoid _get_value() call and if self._Table[val] == None check
    #! _get_value() was unnecessarily long. Coded it in one line below
    def _check_value(self, key):
        val = hash(key) % HashTable.T_SIZE #This is the hash function.
        is_empty = self._Table[val] is None
        return val, is_empty

    def insert(self, key):
        val, is_empty = self._check_value(key)
        col = False #Collision bool
        index = 0
        
        if is_empty: #Empty slot - turn into list of keys to avoid extra cases
            self._Table[val] = [key]

        else: #Collision - append
            self._Table[val].append(key)
            col = True
            index = len(self._Table[val]) - 1

        return val, col, index

    def delete(self, key):
        val, is_empty = self._check_value(key)

        #! It makes no sense to implement a if/else statement if the first branch of
        #!the if returns immediately.
        if is_empty: #Deleting an unexisting element
            return -1, 0

        #! Implement a try/except to avoid doing two lookups
        #! The avoided lookups are <if key in self._Table[val]> and <index = self._Table[val].index(key)>
        try:
            index = self._Table[val].index(key) #This is the O(n) part of the hashtable
            self._Table[val].remove(key)
            return val, index
        except ValueError: # No match was found in list, element does not exist
            return -1, 0
    
    def lookup(self, key):
        val, is_empty = self._check_value(key)

        #! It makes no sense to implement a if/else statement if the first branch of
        #!the if returns immediately.
        if is_empty:
            return -1, 0
        
        #! Implement a try/except to avoid doing two lookups
        #! The avoided lookups are <if key in self._Table[val]> and <index = self._Table[val].index(key)>
        try:
            index = self._Table[val].index(key)
            return val, index
        except ValueError: # No match was found in list, element does not exist
            return -1, 0

    def clear(self):
        self.__init__()

###############
# DRIVER CODE #
###############
def main ():
    # Define actions
    actions = {'i', 'd', 'l', 'c'}

    # Initialize Hash Table
    Table = HashTable()

    # Prompt user for action
    print ("----------------------------------------------------------------------------------------------",
            "\n----------------------------------------------------------------------------------------------",
            "\nPlease enter one of the following commands:",
            "\n\t'i' to insert a value",
            "\n\t'd' to delete a value",
            "\n\t'l' to lookup a value",
            "\n\t'c' to clear the table",
            "\n\tor anything else to quit:")
    action = input("\n\t")

    # Execution While loop
    while (action in actions):
        # Insert
        if action == 'i':      
            key = input("\nPlease enter the value to be inserted:\n")
            val, col, index = Table.insert(key)
            print ("---------------\nOUTPUT:")
            print ("---------------")
            if col:
                print ("\nThere was a collision inserting your key")
                print ("The collision was succesfully handled, and your key '%s' was inserted in slot %i, index %i" % (key, val, index))
            else: print ("\nYour key '%s' was inserted in slot %i, index 0" % (key, val))
        
        # Delete
        elif action == 'd':
            key = input("\nPlease enter the value to be deleted:\n")
            val, index = Table.delete(key)
            print ("---------------\nOUTPUT:")
            print ("---------------")
            if val == -1: print ("ERROR: The specified element does not exist in the table.")
            else:
                print ("\nThe key '%s' was deleted from slot %i, index %i" % (key, val, index))

        # Lookup
        elif action == 'l':
            key = input("\nPlease enter the value to lookup:\n")
            val, index = Table.lookup(key)
            print ("---------------\nOUTPUT:")
            print ("---------------")
            if val == -1:
                print ("The element '%s' does not exist in the table." % key)
            else:
                print ("\nThe key '%s' was found in slot %i, index %i" % (key, val, index))

        elif action == 'c':
            Table.clear()
            print ("---------------\nOUTPUT:")
            print ("---------------")
            print ("Table cleared")

        # Print Table
        print ("\n\nThe full table is:\n", Table._Table)

        # Prompt for next iteration
        print ("\n\n\n----------------------------------------------------------------------------------------------",
                "\nNEW ITERATION"
                "\n----------------------------------------------------------------------------------------------",
                "\nPlease enter one of the following commands:",
                "\n\t'i' to insert a value",
                "\n\t'd' to delete a value",
                "\n\t'l' to lookup a value",
                "\n\t'c' to clear the table",
                "\n\tor anything else to quit:")
        action = input("\n\t")

    print ("\n\nProgram terminated\nPeace out!")

##########################
##########################
if __name__ == "__main__":
    main ()
