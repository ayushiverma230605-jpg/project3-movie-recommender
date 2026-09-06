# Movie Recommendation System (Content-Based Filtering)

A recommendation engine that suggests movies similar to a given title based on genre and plot description, using TF-IDF vectorization and cosine similarity — the same core idea behind "because you watched..." features on streaming platforms.

## Overview

1. **Data** — a curated synthetic dataset of 150 movies with title, genres, description, director, and year (fully offline, no external downloads).
2. **Feature engineering** — genres and descriptions are combined into a single text field, with genres weighted more heavily since they're the strongest similarity signal.
3. **Vectorization** — TF-IDF converts each movie's combined text into a numeric vector.
4. **Similarity** — cosine similarity between all movie vectors powers the `recommend(title, top_n)` function.
5. **Visualization** — similarity score bar chart and genre distribution overview.

## Project Structure

```
project3-movie-recommender/
├── data/
│   └── movies.csv                # generated movie metadata
├── generate_dataset.py           # creates the synthetic dataset
├── movie_recommender.py          # standalone script version
├── Movie_Recommender.ipynb       # notebook walkthrough with visualizations
├── requirements.txt
└── README.md
```

## How to Run

```bash
pip install -r requirements.txt
python3 generate_dataset.py       # generates data/movies.csv
python3 movie_recommender.py      # builds the recommender and prints sample results
```

Or open `Movie_Recommender.ipynb` in Jupyter to explore interactively — try `recommend("Any Movie Title", top_n=5)` on any title in the dataset.

## Example Output

```
Because you watched: 'Legacy of Tomorrow' (Action, 2021)

             title                   genres  year  similarity
 Echoes of Kingdom            Comedy|Action  2006       0.773
       Beyond Void             Crime|Action  2024       0.712
    The Wilderness            Sci-Fi|Action  2014       0.634
```

## Tech Stack

- Python, pandas, scikit-learn, matplotlib

## Possible Extensions

- Swap in a real dataset like MovieLens or TMDB for real titles and posters
- Add collaborative filtering (based on user ratings) alongside content-based filtering
- Wrap it in a simple Streamlit app with a search box and poster images
