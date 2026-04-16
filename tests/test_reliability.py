import pytest
from src.recommender import recommend_songs, load_songs

def test_recommendation_not_empty():
    songs = load_songs("data/songs.csv")
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    recs = recommend_songs(user_prefs, songs, k=3)
    assert len(recs) > 0

def test_explanation_contains_reason():
    songs = load_songs("data/songs.csv")
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}
    recs = recommend_songs(user_prefs, songs, k=1)
    assert "This song" in recs[0][2]

def test_retrieval_fallback():
    songs = load_songs("data/songs.csv")
    user_prefs = {"genre": "nonexistent", "mood": "none", "energy": 0.1}
    recs = recommend_songs(user_prefs, songs, k=2)
    assert len(recs) > 0  # Should fallback to all songs if filter too strict