# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputTriangle1(self):
        print (classify_triangle(201,201,201))
        self.assertEqual(classify_triangle(201,201,201),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle2(self): 
        print (classify_triangle(201,201,1))
        self.assertEqual(classify_triangle(201,201,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle3(self): 
        print (classify_triangle(201,1,201))
        self.assertEqual(classify_triangle(201,1,201),'InvalidInput','Should be InvalidInput')        
    def testInvalidInputTriangle4(self): 
        print (classify_triangle(201,1,1))
        self.assertEqual(classify_triangle(201,1,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle5(self): 
        print (classify_triangle(1,201,201))
        self.assertEqual(classify_triangle(1,201,201),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle6(self): 
        print (classify_triangle(1,201,1))
        self.assertEqual(classify_triangle(1,201,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle7(self): 
        print (classify_triangle(1,1,201))
        self.assertEqual(classify_triangle(1,1,201),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle8(self): 
        print (classify_triangle(200,200,200))
        self.assertNotEqual(classify_triangle(200,200,200),'InvalidInput','Should not be InvalidInput')

    def testInvalidInputTriangle9(self): 
        print (classify_triangle(0,0,0))
        self.assertEqual(classify_triangle(0,0,0),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle10(self): 
        print (classify_triangle(0,0,1))
        self.assertEqual(classify_triangle(0,0,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle11(self): 
        print (classify_triangle(0,1,1))
        self.assertEqual(classify_triangle(0,1,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle12(self): 
        print (classify_triangle(0,1,0))
        self.assertEqual(classify_triangle(0,1,0),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle13(self): 
        print (classify_triangle(1,0,0))
        self.assertEqual(classify_triangle(1,0,0),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle14(self): 
        print (classify_triangle(1,0,1))
        self.assertEqual(classify_triangle(1,0,1),'InvalidInput','Should be InvalidInput')
        
    def testInvalidInputTriangle15(self): 
        print (classify_triangle(1.1,1.1,1.1))
        self.assertEqual(classify_triangle(1.1,1.1,1.1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle16(self): 
        print (classify_triangle(1.1,1,1))
        self.assertEqual(classify_triangle(1.1,1,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle17(self): 
        print (classify_triangle(1,1.1,1))
        self.assertEqual(classify_triangle(1,1.1,1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle18(self): 
        print (classify_triangle(1,1,1.1))
        self.assertEqual(classify_triangle(1,1,1.1),'InvalidInput','Should be InvalidInput')
    def testInvalidInputTriangle19(self): 
        print (classify_triangle(1,1,0))
        self.assertEqual(classify_triangle(1,1,0),'InvalidInput','Should be InvalidInput')

    def testNotATriangle1(self): 
        print (classify_triangle(5,8,3))
        self.assertEqual(classify_triangle(5,8,3),'NotATriangle','Should be NotATriangle')
    def testNotATriangle2(self): 
        print (classify_triangle(5,3,8))
        self.assertEqual(classify_triangle(5,3,8),'NotATriangle','Should be NotATriangle')
    def testNotATriangle3(self): 
        print (classify_triangle(8,3,5))
        self.assertEqual(classify_triangle(8,3,5),'NotATriangle','Should be NotATriangle')
    def testNotATriangle4(self): 
        print (classify_triangle(8,5,3))
        self.assertEqual(classify_triangle(8,5,3),'NotATriangle','Should be NotATriangle')
    def testNotATriangle5(self): 
        print (classify_triangle(3,8,5))
        self.assertEqual(classify_triangle(3,8,5),'NotATriangle','Should be NotATriangle')
    def testNotATriangle6(self): 
        print (classify_triangle(3,5,8))
        self.assertEqual(classify_triangle(3,5,8),'NotATriangle','Should be NotATriangle')

    def testRightTriangle1(self): 
        print (classify_triangle(3,4,5))
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
    def testRightTriangle2(self): 
        print (classify_triangle(3,5,4))
        self.assertEqual(classify_triangle(3,5,4),'Right','3,5,4 is a Right triangle')
    def testRightTriangle3(self): 
        print (classify_triangle(4,3,5))
        self.assertEqual(classify_triangle(4,3,5),'Right','4,3,5 is a Right triangle')
    def testRightTriangle4(self): 
        print (classify_triangle(4,5,3))
        self.assertEqual(classify_triangle(4,5,3),'Right','4,5,3 is a Right triangle')
    def testRightTriangle5(self): 
        print (classify_triangle(5,3,4))
        self.assertEqual(classify_triangle(5,3,4),'Right','5,3,4 is a Right triangle')
    def testRightTriangle6(self): 
        print (classify_triangle(5,4,3))
        self.assertEqual(classify_triangle(5,4,3),'Right','5,4,3 is a Right triangle')
        
    def testEquilateralTriangle1(self): 
        print (classify_triangle(1,1,1))
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    def testEquilateralTriangle2(self): 
        print (classify_triangle(1,2,1))
        self.assertNotEqual(classify_triangle(1,2,1),'Equilateral','1,2,1 should Not be equilateral')
    def testEquilateralTriangle3(self): 
        print (classify_triangle(1,1,2))
        self.assertNotEqual(classify_triangle(1,1,2),'Equilateral','1,1,2 should Not be equilateral')
    def testEquilateralTriangle4(self): 
        print (classify_triangle(2,1,1))
        self.assertNotEqual(classify_triangle(2,1,1),'Equilateral','2,1,1 should Not be equilateral')

    def testScaleneTriangle1(self): 
        print (classify_triangle(5,8,10))
        self.assertEqual(classify_triangle(5,8,10),'Scalene','5,8,10 should be Scalene')
    def testScaleneTriangle2(self): 
        print (classify_triangle(5,8,10))
        self.assertEqual(classify_triangle(5,10,8),'Scalene','5,8,10 should be Scalene')
    def testScaleneTriangle3(self): 
        print (classify_triangle(8,5,10))
        self.assertEqual(classify_triangle(8,5,10),'Scalene','8,5,10 should be Scalene')
    def testScaleneTriangle4(self): 
        print (classify_triangle(8,10,5))
        self.assertEqual(classify_triangle(8,10,5),'Scalene','8,10,5 should be Scalene')
    def testScaleneTriangle5(self): 
        print (classify_triangle(10,5,8))
        self.assertEqual(classify_triangle(10,5,8),'Scalene','10,5,8 should be Scalene')
    def testScaleneTriangle6(self): 
        print (classify_triangle(10,8,5))
        self.assertEqual(classify_triangle(10,8,5),'Scalene','10,8,5 should be Scalene')
    def testScaleneTriangle7(self): 
        print (classify_triangle(3,4,5))
        self.assertNotEqual(classify_triangle(3,4,5),'Scalene','3,4,5 should Not be Scalene')
        
    def testIsocelesTriangle1(self): 
        print (classify_triangle(1,2,2))
        self.assertEqual(classify_triangle(1,2,2),'Isoceles','1,2,2 should be Isoceles')
    def testIsocelesTriangle2(self): 
        print (classify_triangle(2,2,1))
        self.assertEqual(classify_triangle(2,2,1),'Isoceles','2,2,1 should be Isoceles')
    def testIsocelesTriangle3(self): 
        print (classify_triangle(2,1,2))
        self.assertEqual(classify_triangle(2,1,2),'Isoceles','2,1,2 should be Isoceles')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

