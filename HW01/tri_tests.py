import unittest

import classify_tri

class ClassifyTestCase(unittest.TestCase):
    def testRightTriangle(self):
        self.assertEqual(classify_tri.classifyTriangle(3,4,5),
                        'Right Triangle', "Should be a right triangle")
        
    def testEqualateralTriangle(self):
        self.assertEqual(classify_tri.classifyTriangle(3,3,3),
                        'Equalateral Triangle', "Should be an Equalateral")
        
    def testScaleneTriangle(self):
        self.assertEqual(classify_tri.classifyTriangle(1,2,3),
                        'Scalene Triangle', "Should be an Scalene triangle")
        
        self.assertNotEqual(classify_tri.classifyTriangle(5,3,8),
                        'Scalene Triangle', "Not a valid triangle")
        
    def testIsoscelesTriangle(self):
        self.assertEqual(classify_tri.classifyTriangle(3,3,5),
                        'Isosceles Triangle', "Should be an isosceles triangle")        


def suite():
    suite = unittest.TestSuite()
    suite.addTest(ClassifyTestCase('testRightTriangle'))
    suite.addTest(ClassifyTestCase('testEqualateralTriangle'))
    suite.addTest(ClassifyTestCase('testScaleneTriangle'))
    suite.addTest(ClassifyTestCase('testIsoscelesTriangle'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

