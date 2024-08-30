import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib.colors import ListedColormap

# Exemplo de DataFrame
df = pd.read_excel(r'C:\Users\rodri\Documents\hgr\nuvem papavras\nuvem_palavras_frequencia.xlsx')

# Criação do dicionário com palavras e suas frequências
palavras_frequencias = dict(zip(df['palavra'], df['frequência']))

# Carregar a imagem de máscara do seu PC
mascara = np.array(Image.open(r'C:\Users\rodri\Documents\hgr\nuvem papavras\comment.png'))

# Definir a paleta de cores usando matplotlib
cmap = ListedColormap(["#010221", "#0A7373", "#B7BF99", "#EDAA25", "#C43302"])  # Cores personalizadas

# Criação da nuvem de palavras com a máscara e a paleta de cores
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    mask=mascara,
    contour_width=3,
    contour_color='black',
    colormap=cmap  # Aplicando a paleta de cores
).generate_from_frequencies(palavras_frequencias)

# Salvar a nuvem de palavras em um arquivo
wordcloud.to_file('nuvem_de_palavras_com_mascara.png')

# Exibição da nuvem de palavras
plt.figure(figsize=(10, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')  # Remove os eixos
plt.show()
