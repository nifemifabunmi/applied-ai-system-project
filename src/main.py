"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from .recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\nTop recommendations:\n")
    for rec in recommendations:
        song, score, explanation = rec
        print(f"🎵 {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f}")
        print(f"   Reasons: {explanation}")
        print("-" * 40)

    # Example user profiles
    user_profiles = [
        {  # High-Energy Pop
            "genre": "pop",
            "mood": "happy",
            "energy": 0.9,
            "valence": 0.85,
            "danceability": 0.8,
            "tempo_bpm": 125,
            "acousticness": 0.2
        },
        {  # Chill Lofi
            "genre": "lofi",
            "mood": "chill",
            "energy": 0.4,
            "valence": 0.6,
            "danceability": 0.6,
            "tempo_bpm": 75,
            "acousticness": 0.7
        },
        {  # Deep Intense Rock
            "genre": "rock",
            "mood": "intense",
            "energy": 0.95,
            "valence": 0.3,
            "danceability": 0.65,
            "tempo_bpm": 150,
            "acousticness": 0.1
        }
    ]
    for user_profile in user_profiles:
        print(f"\nUser profile: {user_profile}")
        recommendations = recommend_songs(user_profile, songs, k=5)
        print("\nTop recommendations:\n")
        for rec in recommendations:
            song, score, explanation = rec
            print(f"🎵 {song['title']} by {song['artist']}")
            print(f"   Score: {score:.2f}")
            print(f"   Reasons: {explanation}")
            print("-" * 40)


if __name__ == "__main__":
    main()
