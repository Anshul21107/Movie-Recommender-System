import streamlit as st
import pickle
df = pickle.load(open('movies.pkl','rb'))
movies = sorted(df['title'].values)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_idx = df[df['title'] == movie].index[0]
    distances  = similarity[movie_idx]
    movie_list = sorted(list(enumerate(distances)),reverse = True ,key = lambda x:x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
       recommended_movies.append(df.iloc[i[0]].title)
    return recommended_movies


st.title('Movie Recommendation System')
selected_movie_name = st.selectbox(
    'Get five movies similar to this movie',
  movies
)

if st.button('Recommend'):
    # st.write(selected_movie_name)
    recommendation = recommend(selected_movie_name)
    x =0
    for i in recommendation:
        st.write(f"{x+1} {i}")
        x += 1