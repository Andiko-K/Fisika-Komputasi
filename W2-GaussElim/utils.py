from IPython.display import HTML
import numpy as np
import unittest

class TestColumnZero(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestColumnZero, self).__init__(methodName)
        self.func = func
    
    def test_case_1(self):
        M = np.array([[0,2],[1,1]])
        column = 0; start = 0
        result = self.func(M,column,start)
        
        expected_result = 1
        
        self.assertEqual(result, expected_result)
    
    def test_case_2(self):
        M  = np.array([[1,2,3],[0,1,4],[0,0,0]])
        column = 0; start = 2
        result = self.func(M,column,start)
        
        expected_result = False
        
        self.assertEqual(result, expected_result)

    def test_case_3(self):
        M  = np.array([[1,0,3],[1,0,4],[9,0,7]])
        column = 1; start = 0
        result = self.func(M,column,start)
        
        expected_result = False
        
        self.assertEqual(result, expected_result)
    
    def test_case_4(self):
        M  = np.array([[1,4,3],[1,0,4],[9,1,7]])
        column = 1; start = 1
        result = self.func(M,column,start)
        
        expected_result = 2
        
        self.assertEqual(result, expected_result)
        

def run_tests1(func):
    suite = unittest.TestSuite()
    suite.addTest(TestColumnZero('test_case_1', func=func))
    suite.addTest(TestColumnZero('test_case_2', func=func))
    suite.addTest(TestColumnZero('test_case_3', func=func))
    suite.addTest(TestColumnZero('test_case_3', func=func))
    
    runner = unittest.TextTestRunner()
    runner.run(suite)
    
class TestGaussianElimination(unittest.TestCase):
    def __init__(self, methodName='runTest', func=None):
        super(TestGaussianElimination, self).__init__(methodName)
        self.func = func

    def test_case_1(self):
        A = np.array([[2,3],[4,-1]])
        B = np.array([5,1]).reshape(-1,1)
        expected_result = np.array([0.57, 1.28])
        
        result = self.func(A, B)
        
        np.testing.assert_allclose(result.flatten(), expected_result, rtol=1e-2, atol=1e-2)
    
    def test_case_2(self):
        A = np.array([[1,2,3],[2,-1,1], [3,1,-1]])
        B = np.array([9,8,3]).reshape(-1,1)
        expected_result = np.array([ 2.2, -0.8,  2.8])
        
        result = self.func(A, B)
        
        np.testing.assert_allclose(result.flatten(), expected_result, rtol=1e-2, atol=1e-2)

    def test_case_3(self):
        A = np.array([[2,-3,4],[1,0,-1], [3,-1,2]])
        B = np.array([1,2,5]).reshape(-1,1)
        expected_result = np.array([2., 1., 0.])

        
        result = self.func(A, B)
        
        np.testing.assert_allclose(result.flatten(), expected_result, rtol=1e-2, atol=1e-2)
    
    def test_case_4(self):
        A = np.array([[1,2,3],[2,4,6], [3,6,9]])
        B = np.array([1,2,3]).reshape(-1,1)
        expected_result = 'Singular Matrix'

        
        result = self.func(A,B)
        
        self.assertEqual(result, expected_result)

    def test_case_5(self):
        A = np.array([[0,1,1,1],[2,-1,3,-1], [3,1,2,1],[4,-2,1,0]])
        B = np.array([10,5,15,8]).reshape(-1,1)
        expected_result = np.array([ 0.5 , -1.25,  3.5 ,  7.75])

        
        result = self.func(A,B)
        
        np.testing.assert_allclose(result.flatten(), expected_result, rtol=1e-2, atol=1e-2)
    

def run_tests2(func):
    suite = unittest.TestSuite()
    suite.addTest(TestGaussianElimination('test_case_1', func=func))
    suite.addTest(TestGaussianElimination('test_case_2', func=func))
    suite.addTest(TestGaussianElimination('test_case_3', func=func))
    suite.addTest(TestGaussianElimination('test_case_3', func=func))
    suite.addTest(TestGaussianElimination('test_case_5', func=func))
    
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
content_1 = '''
Tukar Baris row1 dengan row2'''

content_2 = '''
<pre><code>
def swap_rows(M, row1, row2):
    M = M.copy()
    M[[row1,row2]] = M[[row2,row1]]
    return M
</code></pre>
'''

content_3 = '''
Kita perlu melakukan iterasi untuk tiap elemen kolom.
Iterasi bertujuan untuk mendapatkan indeks kolom dengan elemen bukan nol pertama.
Fungsi akan memberikan output indeks kolom jika elemen bukan nol ditemukan
'''

content_4 = '''
<pre><code>
def non_zero_column(M, column, row_start=0):
    column_array = M[row_start:, column]
    for i, val in enumerate(column_array):
        if not np.isclose(val, 0, atol = 1e-5):
            index = i+row_start
            return index
    return False
</code></pre>
'''

content_5 = '''
Pada bagian ini, kalian perlu membuat kode yang mampu mendeteksi bila terdapat nilai 0 pada elemen pivot.
Jika terdapat pivot bernilai 0, cari baris dengan elemen bukan nol.
Tukar baris tersebut dengan baris yang telah kita cari.

Anda bisa melihat bagaimana `swap_rows()` dan `non_zero_column()` digabungkan pada kode sebelumnya.
'''

content_6 = '''
Pada bagian kedua, dilakukan operasi aljabar pada tiap baris sesuai dengan apa yang kita pelajari sebelumnya. 
Step 1. Bagi baris dengan nilai pivot
Step 2. Lakukan operasi aljabar pada baris lainnya dengan beracuan elemen pada kolom yang sama dengan kolom pivot
'''

content_7 = '''
<code><pre>
def gaussian_elimination(A,B):

    A = A.copy(); B = B.copy()
    A = A.astype('float64'); B = B.astype('float64')

    M = augmented_matrix(A,B)
    num_rows = M.shape[0]
    
    for row in range(num_rows):
        column = row 
        pivot_candidate = M[row, column]
        
        if np.isclose(pivot_candidate,0) == True:
            pivot_index = non_zero_column(M,column,row)
            M = swap_rows(M, row, pivot_index)
            pivot = M[row,row]
        else: 
            pivot = pivot_candidate
        
        M[row] = M[row]/pivot
        for row2 in range(num_rows):
            if row != row2:
                M[row2]=M[row2]-M[row2,row]*M[row]
                
    result = M[:,-1]            
    return result
</code></pre>
'''
tips1 = tips(title, content_1)
tips2 = tips(title, content_2)
tips3 = tips(title, content_3)
tips4 = tips(title, content_4)
tips5 = tips(title, content_5)
tips6 = tips(title, content_6)
tips7 = tips(title, content_7)
