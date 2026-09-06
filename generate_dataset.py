"""
Generates a movie metadata dataset (title, genres, description, director, year)
for a content-based recommendation system. Fully offline - no downloads needed.
"""

import csv
import random

random.seed(7)

genres_pool = [
    "Action", "Adventure", "Sci-Fi", "Drama", "Comedy", "Romance",
    "Thriller", "Mystery", "Fantasy", "Animation", "Crime", "Horror",
]

description_snippets = {
    "Action": ["a relentless chase across the city", "explosive stunts and high-stakes combat", "a lone hero fighting overwhelming odds"],
    "Adventure": ["an epic journey to a hidden land", "a treasure hunt through uncharted territory", "explorers venturing into the unknown"],
    "Sci-Fi": ["humanity confronts an advanced alien intelligence", "a scientist unravels the mysteries of time travel", "a dystopian future where technology controls society"],
    "Drama": ["a family torn apart by hidden secrets", "one person's struggle to rebuild their life", "a powerful story of loss and redemption"],
    "Comedy": ["a series of hilarious misunderstandings", "an awkward reunion turns into chaos", "a mismatched duo stumbles into absurd situations"],
    "Romance": ["two strangers fall in love against the odds", "a second chance at love years later", "a whirlwind romance set in a foreign city"],
    "Thriller": ["a detective races against time to stop a killer", "nothing is as it seems in this twisting plot", "a conspiracy that reaches the highest levels of power"],
    "Mystery": ["a small town hides a decades-old secret", "an investigator pieces together a baffling case", "clues lead to a shocking revelation"],
    "Fantasy": ["a young hero discovers magical powers", "a kingdom at war with mythical creatures", "an ancient prophecy comes to life"],
    "Animation": ["a heartwarming tale for the whole family", "a colorful world full of unforgettable characters", "an imaginative adventure through a fantastical realm"],
    "Crime": ["a heist that goes horribly wrong", "rival gangs battle for control of the city", "an undercover agent infiltrates a criminal empire"],
    "Horror": ["a haunted house holds a terrifying secret", "survivors are hunted by an unseen evil", "a small group is trapped with something sinister"],
}

title_prefixes = ["The", "Beyond", "Into the", "Shadows of", "Rise of", "Edge of", "Whispers of", "Legacy of", "The Last", "Echoes of"]
title_nouns = ["Horizon", "Tomorrow", "Silence", "Empire", "Storm", "Kingdom", "Fury", "Dream", "Void", "Legacy",
               "Reckoning", "Wilderness", "Labyrinth", "Eclipse", "Frontier", "Requiem", "Ashes", "Odyssey", "Paradox", "Sanctuary"]

directors = ["A. Reyes", "M. Chen", "S. Patel", "J. Novak", "L. Moreau", "K. Adeyemi", "R. Nakamura", "T. O'Brien",
             "D. Alvarez", "C. Petrov", "F. Rossi", "N. Kowalski"]


def make_title(used):
    while True:
        t = f"{random.choice(title_prefixes)} {random.choice(title_nouns)}"
        if t not in used:
            used.add(t)
            return t


rows = []
used_titles = set()

for _ in range(150):
    title = make_title(used_titles)
    n_genres = random.choice([1, 2, 2, 3])
    genres = random.sample(genres_pool, n_genres)
    snippet_parts = [random.choice(description_snippets[g]) for g in genres]
    description = "A story about " + " and ".join(snippet_parts) + "."
    director = random.choice(directors)
    year = random.randint(1995, 2024)
    rows.append((title, "|".join(genres), description, director, year))

with open("data/movies.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "genres", "description", "director", "year"])
    writer.writerows(rows)

print(f"Generated {len(rows)} movies -> data/movies.csv")
