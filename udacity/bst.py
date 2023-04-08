class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self,new_val):
        self.insert_node(self.root,new_val)

    def insert_node(self,node,val):
        if node !=None:
            node=Node(val)
        else:
            if node.value>=val:
                self.insert_node(node.left,val)
            else:
                self.insert_node(node.right,val)

    def search(self, find_val,node='root'):
        if node=='root':
            node = self.root
        if node == None:
            return False
        elif node.value== find_val:
            return True
        elif node.value>=find_val:
            return self.search(find_val,node.left)
        else:
            return self.search(find_val,node.right)


            
        return False
    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)


# Should be True
print (tree.search(4))
# Should be False
print (tree.search(6))