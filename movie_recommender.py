"""
Movie Recommendation System (Content-Based Filtering)
------------------------------------------------------
Recommends movies similar to a given title using TF-IDF on combined
genre + description text, ranked by cosine similarity.

Run: python3 movie_recommender.py
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# 1. Load data
# ---------------------------------------------------------------------------
df = pd.read_csv("data/movies.csv")
print(f"Loaded {len(df)} movies")

# Combine genres + description into one text field, weighting genres higher
# by repeating them, since genre overlap is the strongest similarity signal.
df["combined_features"] = (
    (df["genres"].str.replace("|", " ", regex=False) + " ") * 2 + df["description"]
)

# ---------------------------------------------------------------------------
# 2. Vectorize with TF-IDF
# ---------------------------------------------------------------------------
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined_features"])
print(f"TF-IDF matrix shape: {tfidf_matrix.shape}")

# ---------------------------------------------------------------------------
# 3. Compute cosine similarity between all movies
# ---------------------------------------------------------------------------
similarity_matrix = cosine_similarity(tfidf_matrix)

title_to_index = pd.Series(df.index, index=df["title"]).drop_duplicates()


def recommend(title, top_n=5):
    """Return the top_n movies most similar to the given title."""
    if title not in title_to_index:
        print(f"'{title}' not found in dataset.")
        return pd.DataFrame()

    idx = title_to_index[title]
    scores = list(enumerate(similarity_matrix[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    # Skip index 0 since that's the movie itself
    top_matches = scores[1: top_n + 1]
    movie_indices = [i for i, _ in top_matches]
    similarity_scores = [round(s, 3) for _, s in top_matches]

    result = df.iloc[movie_indices][["title", "genres", "year"]].copy()
    result["similarity"] = similarity_scores
    return result.reset_index(drop=True)


# ---------------------------------------------------------------------------
# 4. Demo recommendations
# ---------------------------------------------------------------------------
sample_titles = df["title"].sample(3, random_state=42).tolist()

for title in sample_titles:
    original = df[df["title"] == title].iloc[0]
    print(f"\n=== Because you watched: '{title}' ({original['genres']}, {original['year']}) ===")
    recs = recommend(title, top_n=5)
    print(recs.to_string(index=False))

# ---------------------------------------------------------------------------
# 5. Visualize similarity scores for one example
# ---------------------------------------------------------------------------
example_title = sample_titles[0]
recs = recommend(example_title, top_n=8)
plt.figure(figsize=(8, 5))
plt.barh(recs["title"], recs["similarity"], color="#4C72B0")
plt.xlabel("Cosine Similarity")
plt.title(f"Top Recommendations for '{example_title}'")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("recommendation_scores.png", dpi=150)
print("\nSaved recommendation_scores.png")

# ---------------------------------------------------------------------------
# 6. Genre distribution overview
# ---------------------------------------------------------------------------
all_genres = df["genres"].str.split("|").explode()
genre_counts = all_genres.value_counts()

plt.figure(figsize=(9, 5))
genre_counts.plot(kind="bar", color="#55A868")
plt.title("Genre Distribution in Dataset")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("genre_distribution.png", dpi=150)
print("Saved genre_distribution.png")
