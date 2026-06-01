import streamlit as st
import pickle
import pandas as pd

st.title('Movie Recommender System')
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movies=pd.DataFrame(movies_dict)

def recommend(movie):
    mov_ind=movies[movies['title']==movie].index[0]  # gives index of given movie
    distances=similarity[mov_ind] # gives mov_ind th row from similarity matrix
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]  # gives nearby next 5 vectors

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



from difflib import get_close_matches 

def find_closest_movie(movie_name): # if user enter wrong name ,it handles
    matches = get_close_matches(movie_name, movies['title'].values, n=1, cutoff=0.6)
    return matches[0] if matches else None

movie_input = st.text_input("Enter a movie name")

if st.button("Recommend"):
    closest_movie = find_closest_movie(movie_input)

    if closest_movie:
        st.success(f"Showing recommendations for: {closest_movie}")
        recommendations = recommend(closest_movie)
        ####
        st.subheader("Recommended Movies")
        for movie in recommendations:
            st.markdown(
                f"""
                <div style="
                    padding: 2px;
                    margin: 2px 0;
                    border-radius: 2px;
                    background-color: #1f2937;
                    border-left: 2px solid #22c55e;
                ">
                    <h4>{movie}</h4>
                </div>
                """,
                unsafe_allow_html=True
            )
        


        ###
       # for movie in recommendations:
         #   st.write(movie)
    else:
        st.error("Movie not found. Please try another movie name.")


    



