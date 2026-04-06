# Código Inicial: Análise de Dados

import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar o dataset (substitua 'data.csv' pelo seu arquivo)
df = pd.read_csv('data.csv')

# 2. Exibir as primeiras 5 linhas
print(df.head())

# 3. Mostrar estatísticas resumidas
print(df.describe())

# 4. (Código de visualização vai aqui)
# Exemplo: df['nome_da_coluna'].hist()
# plt.show()

# Salve seus gráficos como imagens usando plt.savefig('nome_do_arquivo.png')
