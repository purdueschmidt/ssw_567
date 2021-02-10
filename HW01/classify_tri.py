import unittest

def classifyTriangle(a, b, c):
    sides = [a, b, c]
    
    sides.sort(reverse=True)
    
    c_lcl = sides[0]
    a_lcl = sides[1]
    b_lcl = sides[2]
    
    if pow(a_lcl,2) + pow(b_lcl,2) == pow(c_lcl,2):
       return("Right Triangle")
    elif a == b and b == c:
       return("Equalateral Triangle")
    elif a != b and b!=c:
       return("Scalene Triangle")
    elif a == b and b != c:
       return("Isosceles Triangle")
