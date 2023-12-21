# Movie Recommendation System

This repository contains a Python implementation of a movie recommendation system using the TMDB 5000 Movie Dataset. The recommendation system suggests movies based on textual features such as genres, keywords, cast, crew, and production companies. The implementation includes data preprocessing, text vectorization using NLTK, and similarity scoring using cosine similarity.

## Code Documentation

### Data Loading and Preprocessing
- The code loads two CSV files, "tmdb_5000_credits.csv" and "tmdb_5000_movies.csv," containing movie credits and movie details, respectively.
- The datasets are merged based on the movie title, and irrelevant columns are removed.
- Null values are dropped from the dataset.

### Data Transformation Functions
- Several functions (`convert`, `convert1`, `convert2`, `fetch_director`, `fetch_actor`) are defined to convert string representations of lists into actual lists and extract relevant information such as genres, keywords, director, and actors.

### Cleaning and Feature Derivation
- The 'overview' column is tokenized, and certain columns are cleaned by removing spaces.
- A new column 'tags' is derived by combining relevant textual features.
- The 'tags' column is further processed by converting to lowercase and applying stemming.

### Text Vectorization
- NLTK's Porter Stemmer is used for stemming the text.
- Text vectorization is performed using the TfidfVectorizer from scikit-learn with a maximum of 2000 features.

### Similarity Scoring
- Cosine similarity is calculated based on the vectorized text data.
- The `recommend` function takes a movie title as input and returns a list of recommended movie names and their corresponding IDs based on similarity scores.

## Usage
- Ensure the required libraries are installed (`numpy`, `pandas`, `nltk`, `scikit-learn`).
```python
pip install --upgrade numpy pandas nltk scikit-learn
```
- Run the code to load, preprocess, and vectorize the data.
- To open this with streamlit as a web app download all files and install all the dependencies in your virtual Environment
- Write down the given command in your app.py terminal to host it on your local server.
 
```python
streamlit run app.py
```

You can also check the Jupyter notebook for step by step instructions.

Feel free to explore and customize the code for your specific use case.
