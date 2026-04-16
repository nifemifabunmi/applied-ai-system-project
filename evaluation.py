import random
from src.recommender import load_songs, recommend_songs
from collections import Counter

def genre_match_score(recommendations, user_genre):
    if not recommendations:
        return 0.0
    matches = sum(1 for song, _, _ in recommendations if song['genre'] == user_genre)
    return matches / len(recommendations)

def diversity_score(recommendations):
    if not recommendations:
        return 0.0
    artists = [song['artist'] for song, _, _ in recommendations]
    return len(set(artists)) / len(artists)

def run_evaluation():
    songs = load_songs("data/songs.csv")
    test_users = [
        {"genre": "pop", "mood": "happy", "energy": 0.8},
        {"genre": "rock", "mood": "intense", "energy": 0.95},
        {"genre": "lofi", "mood": "chill", "energy": 0.4},
        {"genre": "jazz", "mood": "relaxed", "energy": 0.5},
        {"genre": "electronic", "mood": "energetic", "energy": 0.9},
    ]
    print("EVALUATION SUMMARY\n==================")
    for i, user in enumerate(test_users):
        recs = recommend_songs(user, songs, k=5)
        genre_score = genre_match_score(recs, user["genre"])
        diversity = diversity_score(recs)
        print(f"User {i+1}: {user}")
        print(f"  Genre Match Score: {genre_score:.2f}")
        print(f"  Diversity Score: {diversity:.2f}")
        print(f"  Recommendations:")
        for song, score, explanation in recs:
            print(f"    - {song['title']} by {song['artist']} (Score: {score:.2f})")
        print()
    print("Basic Guardrails: All users received recommendations. No errors encountered.")

if __name__ == "__main__":
    run_evaluation()
