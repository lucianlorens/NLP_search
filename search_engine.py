from sentence_transformers import SentenceTransformer, util

#TODO: convert search_news to another function
#utilities.search_data_point(query, dataframe)

# load model MiniLM
#@st.cache(allow_output_mutation=True)
def load_model():
    return SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

model = load_model()


def search_dataset(query, news_df, column_name):
    query_embedding = model.encode([query], convert_to_tensor=True)
    news_embeddings = model.encode(news_df['stt'].tolist(), convert_to_tensor=True)
    
    # Calcular similaridade
    similarities = util.pytorch_cos_sim(query_embedding, news_embeddings)[0]
    news_df['similarity'] = similarities.cpu().numpy()

    # Ordenar por relevância
    relevant_news = news_df.sort_values(by='similarity', ascending=False).head(4)
    return relevant_news
