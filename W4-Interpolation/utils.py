import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
import unittest
import timeout_decorator

def generate_points(func, num, left_bound = -1, right_bound = 1):
    x = np.linspace(left_bound, right_bound, num)
    y = func(x)
    points = np.c_[x,y]
    return points

piecewise_data = generate_points(lambda x: x**2, 10)

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
    
class TestLagrangeInt(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestLagrangeInt, self).__init__(methodName)
        self.lagrange_int = func
    
    @timeout_decorator.timeout(1)
    def test_case_1(self):
        func = lambda x: 18*x+39
        points = generate_points(func, 2, left_bound = -10, right_bound = 10)
        x = 7
        expected_result = func(x)
        result = self.lagrange_int(x, points)
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
        
    @timeout_decorator.timeout(1)
    def test_case_2(self):
        func = lambda x: x**5+14*x**4+39*x**2+11
        points = generate_points(func, 6, left_bound = -10, right_bound = 10)
        x = 4
        expected_result = func(x)
        result = self.lagrange_int(x, points)
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_3(self):
        func = lambda x: np.cos(x)
        points = generate_points(func, 16, left_bound = -10, right_bound = 10)
        x = 5
        expected_result = func(x)
        result = self.lagrange_int(x, points)
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
def run_tests3(func):
    suite = unittest.TestSuite()
    suite.addTest(TestLagrangeInt('test_case_1', func=func))
    suite.addTest(TestLagrangeInt('test_case_2', func=func))
    suite.addTest(TestLagrangeInt('test_case_3', func=func))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)

def tips(title, content):
    
    return HTML(f'''
    <details>
        <summary>{title}</summary>
        <p>{content}</p>
    </details>
    ''')

title = 'Klik Untuk Melihat Tips!'
content1 = '''
array points berdimensi 2x2, [[x1,y1], [x2,y2]]. Ambil masing-masing nilai x1,y1,x2, dan y2 dalam array dan lakukan operasi dengan variabel x
sehingga didapatkan nilai y interpolasi
'''
content2 = ''' <pre><code>
def linear_int(x, points):
    
    x0, y0 = points[0]
    x1, y1 = points[1]
    
    y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return y
</code></pre>
'''

content3 = '''
Iterasikan tiap nilai x pada x_array. Interpolasi dilakukan menggunakan fungsi linear_int yang telah kita buat sebelumnya terhadap x dan points[index-1:index+1]. (Jika index = 1, interpolasi dilakukan terhadap x dengan baris point[0:2], slicing ini akan mengambil array pada points[0] dan points[1]).
Maka dari itu, pastikan bahwa nilai x berada di rentang points[index-1:index] atau x < points[index]
'''

content4 = '''
#latihan 2
def piecewise_lin(x_array, points):
    y_array = []
    index = 1
    for x in x_array:
        if x > points[index, 0]:
            index += 1
            
        y = linear_int(x, points[index-1:index+1])
        y_array.append(y)

    return y_array
'''

content5 = '''
Lakukan iterasi untuk tiap nilai i dan j. Pada iterasi j, gunakan syarat kondisi sehingga i != j dan gunakan perkalian beruntun (*=) dengan rumus L.
Sementara itu, dengan nilai L yang didapatkan lakukan penjumlahan beruntun (+=) dengan nilai y pada points[i]
'''

content6 = '''
def lagrange_int(x,points):
    result = 0
    n = len(points)-1
    for i in range(0,n+1):
        lagrange_val = 1
        for j in range(0,n+1):
            if not i == j:
                lagrange_val*= ((x-points[j][0])/(points[i][0]-points[j][0]))
        result += lagrange_val*points[i][-1]
    return result
'''
tips1 = tips(title, content1)
tips2 = tips(title, content2)
tips3 = tips(title, content3)
tips4 = tips(title, content4)
tips5 = tips(title, content5)
tips6 = tips(title, content6)