import matplotlib.pyplot as plt

# Dados
x = ['seq',
'1/2',
'1/4',
'1/6',
'1/8',
'1/10 H',
'1/16 H',
'2/2',
'2/4',
'2/6',
'2/8',
'2/10',
'2/16',
'2/32 H']
y = [247.2680,
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

j =[
247.699066,
254.1905313,
92.386621,
55.545506,
61.818517,
60.825757,
64.945801,
340.681939,
107.591951,
69.740689,
53.175621,
54.555039,
43.281455,
49.399033]
w = [
262.113133,
270.961228,
92.922630,
60.014864,
64.585457,
52.592654,
59.191636,
341.172605,
108.400525,
69.526724,
50.348053,
42.858031,
42.315736,
49.339022]

# Criar o gráfico de linhas
plt.plot(x, y, marker='o', label='Rodrigo', color='red')
plt.plot(x, j, marker='s', label='Guilherme', color='skyblue')
plt.plot(x, w, marker='^', label='Pedro', color='green')

plt.xlabel('Núcleos/Threads (H = Hyperthread)')
plt.ylabel('Tempo em segundos')
plt.title('Comparativo execução')
plt.grid(True)
plt.show()


