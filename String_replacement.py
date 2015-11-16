#The first attempt at a string replacement program.

def get_replacement_file(file_name):
    file = open(file_name, 'r')
    string_pairs = {}
    
    for line in file:
        if (line == "\n" or line == ""):
            continue
        line_tokens = line.split()
        #print (line_tokens)
        string_pairs[line_tokens[0]] = line_tokens[1]
        
    return string_pairs

def get_replacement_file_string_to_int(file_name):
    file = open(file_name, 'r')
    string_pairs = {}
    
    for line in file:
        line_tokens = line.split()
        #print (line_tokens)
        string_pairs[line_tokens[0]] = len(string_pairs)
        
    return string_pairs


def process_file(old_file_name, new_file_name, rm_dict):
    """
    Replaces instances of strings (in the format below) which are keys in rm_dict with their values, 
    and outputs it to the file new_file_name.
    new_file_name will be overwritten if it already exists.
    The original file is not modified.
    
    rm_dict = ["a":"b", "c":"d"]
    ---------------------
    a 400
    c 25
    a Other things!
    ---------------------
    
    outputs:
    ---------------------
    b 400
    d 25
    b Other things!
    ---------------------
    """
    in_file = open(old_file_name, 'r')
    out_file = open(new_file_name, 'w')
    
    for line in in_file:
        if (line == "\n" or line == ""):
            continue
        line_tokens = line.split()
        line_tokens[0] = rm_dict[line_tokens[0]]
        for string in line_tokens:
            out_file.write(string)
        out_file.write("\n")



def main():
    rm_dict = get_replacement_file("testfile.txt")
    print (rm_dict)


if __name__ == "__main__":
    main() 































