import pandas as pd
import streamlit as st

import string
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Read in the data.
spot = pd.read_csv('../Data/clean/final.csv')

# Separate my clusters.
cluster_0_songs = spot[spot['km cluster'] == 0]  
cluster_1_songs = spot[spot['km cluster'] == 1]  
cluster_2_songs = spot[spot['km cluster'] == 2]  

#Tokenize
def preprocess_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    tokens = word_tokenize(text)
    return tokens

# Apply text preprocessing to song titles in each cluster
cluster_0_songs['song_tokens'] = cluster_0_songs['song title'].apply(preprocess_text)
cluster_1_songs['song_tokens'] = cluster_1_songs['song title'].apply(preprocess_text)
cluster_2_songs['song_tokens'] = cluster_2_songs['song title'].apply(preprocess_text)

# Create TF-IDF vectorizers for each cluster
tfidf_vectorizer_0 = TfidfVectorizer()
tfidf_vectorizer_1 = TfidfVectorizer()
tfidf_vectorizer_2 = TfidfVectorizer()

# Fit and transform the clusters.
tfidf_matrix_0 = tfidf_vectorizer_0.fit_transform(cluster_0_songs['song_tokens'].apply(lambda x: ' '.join(x)))
tfidf_matrix_1 = tfidf_vectorizer_1.fit_transform(cluster_1_songs['song_tokens'].apply(lambda x: ' '.join(x)))
tfidf_matrix_2 = tfidf_vectorizer_2.fit_transform(cluster_2_songs['song_tokens'].apply(lambda x: ' '.join(x)))

# Applying cosine similarity to each cluster.
cosine_sim_matrix_0 = cosine_similarity(tfidf_matrix_0)
cosine_sim_matrix_1 = cosine_similarity(tfidf_matrix_1)
cosine_sim_matrix_2 = cosine_similarity(tfidf_matrix_2)

#Recommender function.

def recommend_songs(song_title, cluster, cosine_sim_matrix, n=10):
    if song_title not in cluster['song title'].values:
        return "Song not found in this cluster."

    song_index = cluster[cluster['song title'] == song_title].index[0]
    sim_scores = list(enumerate(cosine_sim_matrix[song_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n+1]
    song_indices = [i[0] for i in sim_scores]
    recommended_songs = cluster.iloc[song_indices][['song title', 'artist', 'energy']]
    return recommended_songs

# Streamlit code.
def main():
    st.title("Spotify Cluster Recommender.")
    st.subheader('Based off popularity vs energy.')

    # Input for the song title
    input_song_title = st.text_input("Enter a song title:")

    if st.button("Recommend"):
        # Recommend songs based on the input title
        if input_song_title:
            if input_song_title in cluster_0_songs['song title'].values:
                recommended_songs = recommend_songs(input_song_title, cluster_0_songs, cosine_sim_matrix_0)
            elif input_song_title in cluster_1_songs['song title'].values:
                recommended_songs = recommend_songs(input_song_title, cluster_1_songs, cosine_sim_matrix_1)
            elif input_song_title in cluster_2_songs['song title'].values:
                recommended_songs = recommend_songs(input_song_title, cluster_2_songs, cosine_sim_matrix_2)
            else:
                recommended_songs = "Song not found in any cluster."

            # Display recommendations
            st.header("Top 10 Recommended Songs:")
            st.dataframe(recommended_songs)


if __name__ == "__main__":
    rec = pd.read_csv('../Data/clean/final.csv')
    main()

