import pickle
import requests
import pandas as pd
import streamlit as st

st.title('Movie Recommender System')

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
Movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
# 2daa7ffee94a387ade64b767b27380a9

# Fetching Poster Function  https://image.tmdb.org/t/p/w500//uO2yU3QiGHvVp0L5e5IatTVRkYk.jpg
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2daa7ffee94a387ade64b767b27380a9&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Recommend Function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        # Fetch Poster From Api
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommend_movies_posters

# User Interface
selected_movie_name = st.selectbox('Movies List', Movies_list)

if st.button('Recommend'):
    movie_names, movie_posters = recommend(selected_movie_name)

    pos1, pos2, pos3, pos4, pos5 = st.columns(5)

    with pos1:
        st.text(movie_names[0])
        if movie_posters[0]:
            st.image(movie_posters[0])

    with pos2:
        st.text(movie_names[1])
        if movie_posters[1]:
            st.image(movie_posters[1])

    with pos3:
        st.text(movie_names[2])
        if movie_posters[2]:
            st.image(movie_posters[2])

    with pos4:
        st.text(movie_names[3])
        if movie_posters[3]:
            st.image(movie_posters[3])

    with pos5:
        st.text(movie_names[4])
        if movie_posters[4]:
            st.image(movie_posters[4])
