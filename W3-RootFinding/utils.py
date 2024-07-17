from IPython.display import HTML
import unittest
import timeout_decorator
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
    
    @timeout_decorator.timeout(1)
    def test_case_1(self):
        f = lambda x: 2*np.exp(x)**(.5*x)-3
        x1 = 1; x2 = 2
        result = self.func(f, x1, x2)
        expected_result = False
        
        self.assertEqual(result, expected_result)
    
    @timeout_decorator.timeout(1)
    def test_case_2(self):
        f = lambda x: 3*x**3+5*x**2+2*x-7
        x1 = 0; x2 = 1
        result = self.func(f,x1,x2)
        expected_result = .84
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_3(self):
        f = lambda x: 2*np.sin(x)+np.cos(4*x)+.2*np.tan(x)
        x1 = 2; x2 = 4
        result = self.func(f,x1,x2)
        expected_result = 3.41
    
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
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
    
class TestSecant(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestSecant, self).__init__(methodName)
        self.func = func
    
    @timeout_decorator.timeout(1)
    def test_case_1(self):
        f = lambda x: 2*np.exp(x)**(.5*x)-3
        x1 = 2.1; x2 = 2
        result = self.func(f, x1, x2)
        expected_result = 0.90
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_2(self):
        f = lambda x: 3*x**3+5*x**2+2*x-7
        x1 = 3; x2 = 2.9
        result = self.func(f,x1,x2)
        expected_result = .84
        
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_3(self):
        f = lambda x: 2*np.sin(x)+np.cos(4*x)+.2*x
        x1 = 3.2; x2 = 3
        result = self.func(f,x1,x2)
        expected_result = 3.524
    
        self.assertAlmostEqual(result, expected_result, delta = 1e-3)
    
    @timeout_decorator.timeout(1)
    def test_case_4(self):
        f = lambda x: (x-70)*(x**2-8*x)+10
        x1 = 60; x2 = 61
        result = self.func(f,x1,x2)
        expected_result = 69.99
    
        self.assertAlmostEqual(result, expected_result, delta = 1e-2)

def run_tests2(func):
    suite = unittest.TestSuite()
    suite.addTest(TestSecant('test_case_1', func=func))
    suite.addTest(TestSecant('test_case_2', func=func))
    suite.addTest(TestSecant('test_case_3', func=func))
    suite.addTest(TestSecant('test_case_4', func=func))
    
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
Syarat dari teorema nilai tengah ialah f(x1) dan f(x2) perlu memiliki tanda yang berlawanan. Dengan demikian jika f(x1)*f(x2) bernilai positif, tidak ada nilai akar di antaranya.'''
content2 = '''
Buat while loop di mana program akan terus berjalan apabila f(xt) bernilai lebih dari e (nilai toleransi). Jangan lupa pastikan agar tidak terjadi infinite loop. fungsi run_test1 akan memperingatkan Anda dengan timeout warning.
'''
content3 =  ''' <pre><code>
def bisection(f,x1,x2,e = 1e-3): 

    if f(x1)*f(x2) > 0:   
        return False
    
    xt = (x1+x2)/2
    while abs(f(xt)) >= e:
        if f(xt)*f(x1) <= 0:
            x2 = xt
        else:
            x1 = xt
        xt = (x1+x2)/2
    return xt
</code></pre>
'''
content4 = '''
Kita tidak perlu menginisialisasi nilai xt seperti sebelumnya. Melainkan, kita hanya perlu meninjau apakah f(x2) bernilai lebih dari e
'''
content5 = content3 =  ''' <pre><code>
def secant(f,x1,x2,e = 1e-3): 
    while abs(f(x2)) >= e:
    
        derivative = (f(x1)-f(x2))/(x1-x2)
        x_value = x2 -f(x2)/derivative
        x1 = x2
        x2 = x_value

    return x2
</code></pre>
'''

tips1 = tips(title, content1)
tips2 = tips(title, content2)
tips3 = tips(title, content3)
tips4 = tips(title, content4)
tips5 = tips(title, content5)