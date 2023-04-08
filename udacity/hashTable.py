"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        key=self.calculate_hash_value(string)
        self.table[key]=string
        

    def lookup(self, string):
        key=self.calculate_hash_value(string)
        if self.table[key] == string:
            return key
        return -1

    def calculate_hash_value(self, string):
        dt=[ord(x) for x in string]
        return dt[0]*100+dt[1]
    
# Setup
hash_table = HashTable()
hash_table.store('UDACITY')
li = [23, 56, 87, 12]
li.sort(reverse=False)
print(li)

# Test calculate_hash_value
# Should be 8568
# print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
# print hash_table.lookup('UDACITY')

# Test store
# hash_table.store('UDACITY')
# Should be 8568
# print hash_table.lookup('UDACITY')

# Test store edge case
# hash_table.store('UDACIOUS')
# Should be 8568
# print hash_table.lookup('UDACIOUS')
