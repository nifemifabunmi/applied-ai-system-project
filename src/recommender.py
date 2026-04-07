from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def score_song(self, song: Song, user: UserProfile) -> float:
        score = 0.0
        if song.genre == user.favorite_genre:
            score += 2.5
        if song.mood == user.favorite_mood:
            score += 1.5
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff <= 0.05:
            energy_bonus = 1.0
        elif energy_diff <= 0.15:
            energy_bonus = 0.9 - (energy_diff * 0.5)
        else:
            energy_bonus = 1.0 - (energy_diff * 3)
        score += energy_bonus
        if user.likes_acoustic:
            score += song.acousticness * 0.6
        else:
            score -= song.acousticness * 0.6
        return score

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        scored = [(song, self.score_song(song, user)) for song in self.songs]
        scored.sort(key=lambda x: x[1], reverse=True)
        return [song for song, _ in scored[:k]]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        reasons = []
        if song.genre == user.favorite_genre:
            reasons.append(f"matches your favorite genre '{user.favorite_genre}'")
        if song.mood == user.favorite_mood:
            reasons.append(f"matches your favorite mood '{user.favorite_mood}'")
        energy_diff = abs(song.energy - user.target_energy)
        if energy_diff < 0.1:
            reasons.append("has energy level very close to your target")
        elif energy_diff < 0.3:
            reasons.append("has energy level somewhat close to your target")
        if user.likes_acoustic and song.acousticness > 0.5:
            reasons.append("is acoustic, which you prefer")
        elif not user.likes_acoustic and song.acousticness < 0.3:
            reasons.append("is not very acoustic, matching your preference")
        if reasons:
            return f"This song {', '.join(reasons)}."
        else:
            return "This song may not perfectly match your preferences, but give it a listen!"

def load_songs(csv_path: str) -> List[Dict]:
    """
    Loads songs from a CSV file.
    Required by src/main.py
    """
    import csv
    songs = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            song = {
                'id': int(row['id']),
                'title': row['title'],
                'artist': row['artist'],
                'genre': row['genre'],
                'mood': row['mood'],
                'energy': float(row['energy']),
                'tempo_bpm': float(row['tempo_bpm']),
                'valence': float(row['valence']),
                'danceability': float(row['danceability']),
                'acousticness': float(row['acousticness']),
            }
            songs.append(song)
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    favorite_genre = user_prefs.get('genre', '')
    favorite_mood = user_prefs.get('mood', '')
    target_energy = user_prefs.get('energy', 0.5)
    likes_acoustic = user_prefs.get('likes_acoustic', False)
    
    def score_song(song: Dict) -> float:
        score = 0.0
        if song['genre'] == favorite_genre:
            score += 2.5
        if song['mood'] == favorite_mood:
            score += 1.5
        energy_diff = abs(song['energy'] - target_energy)
        if energy_diff <= 0.05:
            energy_bonus = 1.0
        elif energy_diff <= 0.15:
            energy_bonus = 0.9 - (energy_diff * 0.5)
        else:
            energy_bonus = 1.0 - (energy_diff * 3)
        score += energy_bonus
        if likes_acoustic:
            score += song['acousticness'] * 0.6
        else:
            score -= song['acousticness'] * 0.6
        return score
    
    def explain_song(song: Dict) -> str:
        reasons = []
        if song['genre'] == favorite_genre:
            reasons.append(f"matches your favorite genre '{favorite_genre}'")
        if song['mood'] == favorite_mood:
            reasons.append(f"matches your favorite mood '{favorite_mood}'")
        energy_diff = abs(song['energy'] - target_energy)
        if energy_diff < 0.1:
            reasons.append("has energy level very close to your target")
        elif energy_diff < 0.3:
            reasons.append("has energy level somewhat close to your target")
        if likes_acoustic and song['acousticness'] > 0.5:
            reasons.append("is acoustic, which you prefer")
        elif not likes_acoustic and song['acousticness'] < 0.3:
            reasons.append("is not very acoustic, matching your preference")
        if reasons:
            return f"This song {', '.join(reasons)}."
        else:
            return "This song may not perfectly match your preferences, but give it a listen!"
    
    scored = [(song, score_song(song), explain_song(song)) for song in songs]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[:k]
