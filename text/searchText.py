import re
import os
from collections import Counter, defaultdict

# Definindo a Blacklist
BLACKLIST = {"a", "automutilação", "suicídio", "violência"}

def ler_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        texto = file.read()
    return texto

def formatar_texto(texto):
    # Converter para lowercase
    texto = texto.lower()
    # Remover caracteres especiais e pontuação, manter apenas letras e espaços
    texto = re.sub(r'[^a-z\s]', '', texto)
    # Remover espaços duplicados
    texto = re.sub(r'\s+', ' ', texto).strip()
    return texto

def filtrar_palavras(texto, blacklist):
    palavras_filtradas = [palavra for palavra in re.findall(r'\b\w+\b', texto.lower()) if palavra not in blacklist]
    return ' '.join(palavras_filtradas)

def processar_texto(texto):
    palavras = re.findall(r'\b\w+\b', texto.lower())
    palavras_unicas = sorted(set(palavras))
    return palavras, palavras_unicas

def contar_ocorrencias(palavras):
    contagem = Counter(palavras)
    return contagem

def encontrar_ngramas(palavras, n=2):
    ngramas = defaultdict(int)
    for i in range(len(palavras) - n + 1):
        ngrama = tuple(palavras[i:i+n])
        ngramas[ngrama] += 1
    return ngramas

def salvar_em_arquivo(caminho_arquivo, linhas):
    with open(caminho_arquivo, 'w', encoding='utf-8') as file:
        for item in linhas:
            file.write(f"{item}\n")


def main(caminho_arquivo):
    texto = ler_arquivo(caminho_arquivo)
    texto_formatado = formatar_texto(texto)  # Formatar o texto antes de qualquer outra operação
    texto_filtrado = filtrar_palavras(texto_formatado, BLACKLIST)
    palavras, palavras_unicas = processar_texto(texto_filtrado)
    contagem_palavras = contar_ocorrencias(palavras)
    bigramas = encontrar_ngramas(palavras, 2)
    trigramas = encontrar_ngramas(palavras, 3)
    
    # Criar diretório de saída se não existir
    os.makedirs('output', exist_ok=True)
    
    # print("Palavras únicas (ordenadas):", palavras_unicas)
    # print("Contagem de palavras:", contagem_palavras)
    # print("Bigramas mais comuns:", sorted(bigramas.items(), key=lambda item: item[1], reverse=True))
    # print("Trigramas mais comuns:", sorted(trigramas.items(), key=lambda item: item[1], reverse=True))
    
    salvar_em_arquivo('output/palavras_unicas.txt', palavras_unicas)
    salvar_em_arquivo('output/contagem_palavras.txt', [f"{palavra}: {contagem}" for palavra, contagem in contagem_palavras.items()])
    salvar_em_arquivo('output/bigramas_comuns.txt', [f"{bigrama}: {contagem}" for bigrama, contagem in sorted(bigramas.items(), key=lambda item: item[1], reverse=True)])
    salvar_em_arquivo('output/trigramas_comuns.txt', [f"{trigrama}: {contagem}" for trigrama, contagem in sorted(trigramas.items(), key=lambda item: item[1], reverse=True)])


if __name__ == "__main__":
    caminho_arquivo = 'book.txt'
    main(caminho_arquivo)
