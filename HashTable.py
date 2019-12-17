##############################
# Created by Samuelito Perro
# This is a program that implements a HashTable using only lists (and technically sets too)
# Collision Handling done with Separate Chaining using sets
##############################
import sys

class HashTable:
    # Initialize the table with a fixed size of 54 slots
    def __init__(self):
        self.Table = [None] * 54

    def _get_value(self, key): #This is my hash function.
        # It finds the hash of every string. total % 54
        total = hash(key)
        return total % 54

    def insert(self, key):
        val = self._get_value(key)
        col = False #Collision bool
        index = 0
        
        if self.Table[val] == None: #Empty slot - turn into list of keys to avoid extra cases
            self.Table[val] = [key]

        else: #Collision - append
            self.Table[val].append(key)
            col = True
            index = len(self.Table[val]) - 1

        return val, col, index

    def delete(self, key):
        val = self._get_value(key)

        if self.Table[val] == None: #Deleting an unexisting element
            return -1, 0

        elif key in self.Table[val]: #This is the O(n) part of the hashtable
            index = self.Table[val].index(key)
            self.Table[val].remove(key)
            return val, index

        else: # No match was found in list, element does not exist
            return -1, 0
    
    def lookup(self, key):
        val = self._get_value(key)

        if self.Table[val] == None:
            return -1, 0
        else:
            if key in self.Table[val]:
                index = self.Table[val].index(key)
                return val, index

            # No match was found in list, element does not exist
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
        print ("\n\nThe full table is:\n", Table.Table)

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
if __name__ == "__main__":
    main ()