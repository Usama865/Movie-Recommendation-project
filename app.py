import streamlit as st
from Helper_file import movies
from Helper_file import recommend
import numpy as np
import requests as rq
import json
import nltk 



title=st.title("Movie Recommendation System")

def movie_poster(movie_id: int):
    response= rq.get("https://api.themoviedb.org/3/movie/{}?api_key=ddf1b64692217b6f9abb5a88eab481a1&language=en-US".format(movie_id))
    poster_data= response.json()
    url="http://image.tmdb.org/t/p/w500" + poster_data['poster_path'] 
    return url


select_bar=st.selectbox("Enter Movie Name Here:",movies["title"])
result=recommend(select_bar)

# for poster 
poster_result=[]
for i in result["id"]:
    poster_result.append(movie_poster(i))


## Button Logic
if st.button("Get Recommendations"):

    col_elements = st.columns(len(result["id"]))

    for col_index, col in enumerate(col_elements):
        current_id = result['id'][col_index]
        current_name = result['names'][col_index]  # Assuming 'names' is a list corresponding to each 'id'
        current_poster= poster_result[col_index]

        with col:
            st.header(current_name)
            st.image(current_poster)


    
    
    
    
    
    
    
    
    
    

