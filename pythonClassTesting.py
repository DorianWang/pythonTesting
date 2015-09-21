class BinaryTree:
    
    node_left = 0
    node_right = 0
    compare_function = 0
    new_compare = False
    data = 0
    
    def __init__(self, new_data):
        data = new_data
        
    
    def set_compare(new_compare_function):
        """ (function)
        Sets the function the tree should use to compare inputted data.
        This function must take 2 inputs, and return true if they are in
        the correct order.
        """
        compare_function = new_compare_function
        new_compare = True
    
    def set_compare_all(new_compare_function):
        """ (function)
        Sets the function the tree should use to compare inputted data.
        This function must take 2 inputs, and return true if they are in
        the correct order.
        """
        set_compare(new_compare_function)
        for x in collection:
            x.set_compare_all(new_compare_function)
    
    def add_node(input_data):
        if new_compare:
            if (compare_function(input_data, data)):
                pass
    


