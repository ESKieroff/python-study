import matplotlib.pyplot as plt

# Dados
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # "explode" a slice

# Criar o gráfico de pizza
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)

plt.axis('equal')  # Assegura que o gráfico é desenhado como um círculo.
plt.title('Gráfico de Pizza')
plt.show()
