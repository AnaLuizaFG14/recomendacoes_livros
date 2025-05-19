import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity

def tratamento_texto(texto):
    texto = str(texto).lower()
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(texto)
    stop_words = set(stopwords.words("english"))
    tokens = [palavra for palavra in tokens if palavra not in stop_words]
    return ' '.join(tokens)

def recomendacao_livro(consulta):
# 1. Carregar o dataset
    df = pd.read_csv('livros.csv')

    # 2. Padronizar títulos para comparação (sem alterar os originais)
    df['titulo_lower'] = df['titulo'].str.strip().str.lower()

    # 3. Remover títulos duplicados (ignorando maiúsculas/minúsculas)
    df = df.drop_duplicates(subset='titulo_lower', keep='first').reset_index(drop=True)

    df['descricao'] = df['descricao'].apply(tratamento_texto)

    # 4. Vetores e colunas
    titles = df['titulo']
    descriptions = df['descricao'].fillna('')
    editoras = df['editora']
    autor = df['autor']

    # 5. Vetorizar descrições
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(descriptions)

    # 6. Entrada do usuário (busca sem case sensitive)
    # while True:
    #     user_input = input("\nDigite o nome de um livro: ").strip().lower()
    #     if user_input in df['titulo_lower'].values:
    #         break
    #     else:
    #         print(f"❌ Livro '{user_input}' não encontrado. Tente novamente.")

    # 7. Encontrar índice do livro
    idx = df[df['titulo_lower'] == consulta.strip().lower()].index[0]

    # 8. Calcular similaridade
    sim_scores = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()

    # 9. Montar ranking com título, editora e similaridade
    similar_books = pd.DataFrame({
        'Livro': titles,
        'Editora': editoras,
        'Autor(a)': autor,
        'Similaridade': sim_scores
    })

    # 10. Remover o próprio livro e ordenar
    similar_books = similar_books[similar_books.index != idx]
    return similar_books.sort_values(by='Similaridade', ascending=False)

    # 11. Mostrar resultado
