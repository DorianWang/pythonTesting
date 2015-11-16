class BinaryTree:
    
    node_left = None
    node_right = None
    compare_function = None
    new_compare = False
    data = None
    
    def __init__(self, new_data):
        self.data = new_data
        
    
    def set_compare(self, new_compare_function):
        """ (function)
        Sets the function the tree should use to compare inputted data.
        This function must take 2 inputs, and return true if they are in
        the correct order.
        """
        self.compare_function = new_compare_function
        self.new_compare = True
        
    
    def set_compare_all(self, new_compare_function):
        """ (function)
        Sets the function the tree should use to compare inputted data.
        This function must take 2 inputs, and return true if they are in
        the correct order.
        """
        self.set_compare(new_compare_function)
        if (self.node_left is not None):
            self.node_left.set_compare_all(new_compare_function)
        if (self.node_right is not None):
            self.node_right.set_compare_all(new_compare_function)
        
    
    def add_node(self, input_data):
        """ (data_type)
        Adds a new node to the tree. Will create new nodes if required.
        Uses the user set compare function if it has been set.
        """
        if self.new_compare:
            if (self.compare_function(input_data, self.data)):
                if (self.node_left == None):
                    self.node_left = BinaryTree(input_data)
                else:
                    self.node_left.add_node(input_data)
            else:
                if (self.node_right == None):
                    self.node_right = BinaryTree(input_data)
                else:
                    self.node_right.add_node(input_data)
        else:
            if (input_data < self.data):
                if (self.node_left == None):
                    self.node_left = BinaryTree(input_data)
                else:
                    self.node_left.add_node(input_data)
            else:
                if (self.node_right == None):
                    self.node_right = BinaryTree(input_data)
                else:
                    self.node_right.add_node(input_data)         
                    
                    
    def _output_tree(self, l):
        """ (None) -> list
        Returns the contents of the tree in the form of a list, from "left to right".
        This is not flattened
        """
        
        if (self.node_left is not None):
            self.node_left._output_tree(l)
        
        l.append(self.data)
        
        if (self.node_right is not None):
            self.node_right._output_tree(l)      
                
    def output_tree(self):
        """ (None) -> list
        Returns the contents of the tree in the form of a list, from "left to right".
        """
        l = list()

        
        if (self.node_left is not None):
            self.node_left._output_tree(l)
        
        l.append(self.data)
        
        if (self.node_right is not None):
            self.node_right._output_tree(l)
        
        return l








