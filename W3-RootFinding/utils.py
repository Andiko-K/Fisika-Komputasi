from IPython.display import HTML
import unittest
import numpy as np
import matplotlib.pyplot as plt

def graph(f, x_root, left_bound = -5, right_bound = 2, upper_bound = 20, lower_bound = -10):
    '''Graph the given function f and the root point based on x_root'''
    x = np.linspace(left_bound, right_bound, 100)
    y = f(x)
    
    fig, ax = plt.subplots(figsize = (5,3))
    ax.set_ylim(lower_bound, upper_bound)
    ax.set_xlim(left_bound, right_bound)
    ax.grid()
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('gray')
    ax.spines['top'].set_color('none')
    
    ax.set_title(r'Nilai Akar Persamaan', fontsize = 10)
    ax.plot(x,y, color = 'black')
    ax.scatter(x_root, f(x_root), color = 'red', label = f'({x_root:.2f}, {f(x_root):.2f})')
    ax.legend(loc = 'best')
    
    plt.plot()
    
class TestBisection(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestBisection, self).__init__(methodName)
        self.func = func
    
    def test_case_1(self):
        f = lambda x: 2*np.exp(x)**(.5*x)-3
        x1 = 1; x2 = 2
        result = self.func(f, x1, x2)
        expected_result = False
        
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        f = lambda x: 3*x**3+5*x**2+2*x-7
        x1 = 0; x2 = 1
        result = self.func(f,x1,x2)
        expected_result = .84
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    def test_case_3(self):
        f = lambda x: 2*np.sin(x)+np.cos(4*x)+.2*np.tan(x)
        x1 = 2; x2 = 4
        result = self.func(f,x1,x2)
        expected_result = 3.41
    
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    def test_case_4(self):
        f = lambda x: (x-70)*(x**2-8*x)+10
        x1 = 60; x2 = 200
        result = self.func(f,x1,x2)
        expected_result = 69.99
    
        self.assertAlmostEqual(result, expected_result, delta = 1e-2)

def run_tests1(func):
    suite = unittest.TestSuite()
    suite.addTest(TestBisection('test_case_1', func=func))
    suite.addTest(TestBisection('test_case_2', func=func))
    suite.addTest(TestBisection('test_case_3', func=func))
    suite.addTest(TestBisection('test_case_4', func=func))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)