import matplotlib.pyplot as plt
import numpy as np

# Dados
data = [247.2680,
256.5948,
93.007152,
71.429429,
47.626222,
40.539512,
50.832475,
326.587672,
103.275395,
66.384870,
49.355554,
50.692451,
43.175392,
47.898888]

# Criar o histograma
plt.hist(data, bins=30, alpha=1, color='blue')

plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.title('Histograma')
plt.grid(True)
plt.show()
