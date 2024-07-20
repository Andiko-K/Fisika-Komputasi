import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
import unittest
import timeout_decorator

class TestLinearInt(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestLinearInt, self).__init__(methodName)
        self.linear_int = func
    
    @timeout_decorator.timeout(1)
    def test_case_1(self):
        points =  np.array([[1,6],[5,10]])
        x = 2
        expected_result = 7.0
        result = self.linear_int(x, points)
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_2(self):
        points =  np.array([[10,49],[30,-20]])
        x = 15
        expected_result = 31.75
        result = self.linear_int(x, points)
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_3(self):
        points = np.array([[-10,49],[-20,-20]])
        x = -16
        expected_result = 7.60
        result = self.linear_int(x, points)
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)

def run_tests1(func):
    suite = unittest.TestSuite()
    suite.addTest(TestLinearInt('test_case_1', func=func))
    suite.addTest(TestLinearInt('test_case_2', func=func))
    suite.addTest(TestLinearInt('test_case_3', func=func))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

class TestPiecewiseInt(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestPiecewiseInt, self).__init__(methodName)
        self.piecewise_int = func
    
    @timeout_decorator.timeout(1)
    def test_case_1(self):
        points_x = np.linspace(-1,1,20)
        points = np.c_[points_x, points_x**2]
        
        x = np.linspace(-1,1,100)
        expected_result = x**2
        result = self.piecewise_int(x, points)
        
        np.testing.assert_allclose(result, expected_result, rtol=1e-2, atol=1e-2)

def run_tests2(func):
    suite = unittest.TestSuite()
    suite.addTest(TestPiecewiseInt('test_case_1', func=func))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

def generate_points(func, num, left_bound = -1, right_bound = 1):
    x = np.linspace(left_bound, right_bound, num)
    y = func(x)
    points = np.c_[x,y]
    return points

piecewise_data = generate_points(lambda x: x**2, 10)