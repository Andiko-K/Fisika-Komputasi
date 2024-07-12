from IPython.display import HTML
import numpy as np
import math
import matplotlib.pyplot as plt

def visualize(predict_func, truth, iteration):
    truth_func = {'sin': math.sin, 'cos': math.cos}
    array = np.linspace(0,2*np.pi,100)
    func = lambda x, iteration = iteration: predict_func(x, iteration)
    prediction = np.vectorize(func)(array)
    ground_truth = np.vectorize(truth_func[truth])(array)
    
    loss = np.sqrt(np.mean((prediction-ground_truth)**2))
    color = 'blue'
    
    fig, ax = plt.subplots(figsize = (6,4))
    ax.plot(array, prediction, 'b', label = 'Numerik')
    ax.plot(array, ground_truth, 'r--', label = 'Analitik')
    ax.plot([], [], ' ', label=f'Loss: {loss:.4f}')
    ax.legend()
    ax.set_ylim(-1.5, 1.5)
    ax.grid()
    
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    
    if  loss > 1e-3:
        raise ValueError(f'''
        Loss value between Prediction and Ground Truth value is too big!
        Change your iteration numbers or your code in general!''')
    else:
        print("Kode Anda Sudah Benar! Lanjutkan pada Tahap Selanjutnya!")
def test_1(factorial):
    random_numbers = np.random.choice(np.arange(1, 11), 5, replace=False)
    ground_truth = np.vectorize(math.factorial)(random_numbers)
    prediction = np.vectorize(factorial)(random_numbers)
    
    if np.sum(prediction-ground_truth) != 0:
        raise ValueError(f'''
        Given array of numbers: {np.array2string(random_numbers, separator = ',')};
        Returned: {np.array2string(prediction, separator = ',')}
        As opposed to expected value: {np.array2string(ground_truth, separator = ',')}
        
        Please fix your code!''')
    print("Kode Anda Sudah Benar! Lanjutkan pada Tahap Selanjutnya!")


def tips(title, content):
    
    return HTML(f'''
    <details>
        <summary>{title}</summary>
        <p>{content}</p>
    </details>
    ''')

title = 'Klik Untuk Melihat Tips!'
content_f1 = '''
Gunakan Iterasi While Loop, For Loop, atau Rekursif untuk mendapatkan nilai faktorial!

Perlu diingat bahwa perulangan dimulai dari angka 0 dan berhenti ketika mencapai angka n!
'''
content_f2 = '''
Contoh Jawaban: 

<pre><code>
def factorial(x):
    value = 1
    for n in range(x):
        value *= (n+1)
    return value
</code></pre>
'''
content_s1 = '''
Untuk tiap perulangan, variabel value perlu ditambahkan dengan aproksimasi Deret Maclauren untuk sin(x).'''

content_c1 = '''
Sama seperti fungsi sin(x), variabel value perlu ditambahkan dengan aproksimasi Deret Maclauren untuk cos(x).'''
f1 = tips(title, content_f1)
f2 = tips(title, content_f2)
s1 = tips(title, content_s1)
c1 = tips(title, content_c1)