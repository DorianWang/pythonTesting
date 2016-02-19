"""
SYSC 1005 Fall 2015 Lab 9, Parts 2 and 3
"""

def get_points():
    """ Return a set of (x, y) points, with each point stored in a tuple.
    """
    return {(1.0, 5.0), (2.0, 8.0), (3.5, 12.5)}


def fit_lines_to_points(pts):
    """
    Fits a line to points using least squares regression.
    List (Tuple) -> Tuple
    """
    sumX = sum (pt[0] for pt in pts)
    sumY = sum (pt[1] for pt in pts)
    sumX2 = sum (pt[0] ** 2 for pt in pts)
    sumXY = sum (pt[0] * pt[1] for pt in pts)
    nPt = len(pts)
    
    return ((sumX * sumY - nPt * sumXY) / (sumX ** 2 - nPt * sumX2), 
            (sumX * sumXY - sumX2 * sumY) / (sumX ** 2 - nPt * sumX2))

def read_and_print_lines():
    file = open("data.txt", 'r')
    for line in file:
        print(line)
    file.close()

def read_points(filename):
    """
    Returns the points within the file filename.
    String -> Set (Tuple)
    """
    file = open(filename, 'r')
    a = set()
    for line in file:
        #Not using external libraries
        b = list(filter(None, line.split(" ")))
        a.add((float(b[0]), float(b[1])))  
    return a


if __name__ == "__main__":
    inputThings = input("Please enter the name of the input file.\n")
    print ("The best fit line is y = {0}x + {1}."
           .format(*fit_lines_to_points(read_points(inputThings))))

