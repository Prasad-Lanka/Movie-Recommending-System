# Movie-Recommending-System
A simple recommender that suggests similar type of movies
# 🎬 Movie Recommender System

A Content-Based Movie Recommendation System built using Python, Machine Learning, and Streamlit. The application recommends movies similar to a selected movie by analyzing movie metadata such as genres, keywords, cast, and crew.

##  Features

- Recommend Top 5 Similar Movies
- Content-Based Filtering
- Cosine Similarity-Based Recommendations
- Interactive Streamlit Interface
- Fast and Lightweight

##  Tech Stack

- Python
- Pandas
- Scikit-Learn
- NLTK
- Streamlit
- Pickle

## How It Works

1. Movie metadata is collected and preprocessed.
2. Important features (genres, keywords, cast, crew) are combined into tags.
3. Text data is vectorized using CountVectorizer.
4. Cosine Similarity is calculated between movie vectors.
5. The system recommends the most similar movies.

## Project Structure

```text
Movie-Recommender-System/
│
├── app.py
├── movie_recommend.ipynb
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
└── README.md
```

## Run Locally

```bash
git clone https://github.com/Prasad-Lanka/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt
streamlit run app.py
```

## Future Improvements

- Movie Poster Integration
- TMDB API Support
- Search Autocomplete
- Genre-Based Filtering
- Hybrid Recommendation System

## Author

Prasad Lanka

B.Tech CSE-AIML

GitHub: https://github.com/Prasad-Lanka
This project uses the TMDB 5000 Movie ,TMDB 5000 credits datasets.  
Due to file size limitations, the datasets are not included in this repository.

Dataset source: TMDB 5000 Movie Dataset ,TMDB 5000Credits Dataset from Kaggle.

To run the notebook from scratch, download the dataset and place the CSV files in the project folder.
