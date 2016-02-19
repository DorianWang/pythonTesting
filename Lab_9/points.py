import math
#import linear_regression as lin_regr

def distance(pt1, pt2):
    """
    Returns the distance between two points.
    Tuple, Tuple -> Float
    """
    return math.sqrt((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2 )

