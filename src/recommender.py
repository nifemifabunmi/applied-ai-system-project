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
                'popularity': int(row.get('popularity', 50)),
                'release_decade': row.get('release_decade', ''),
                'detailed_mood': row.get('detailed_mood', ''),
                'instrumentalness': float(row.get('instrumentalness', 0.0)),
                'language': row.get('language', 'English'),
            }
            songs.append(song)
    return songs

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """
    Functional implementation of the recommendation logic.
    Required by src/main.py
    """
    import logging
    logging.basicConfig(level=logging.INFO)

    favorite_genre = user_prefs.get('genre', '')
    favorite_mood = user_prefs.get('mood', '')
    target_energy = user_prefs.get('energy', 0.5)
    likes_acoustic = user_prefs.get('likes_acoustic', False)
    favorite_decade = user_prefs.get('release_decade', '')
    favorite_detailed_mood = user_prefs.get('detailed_mood', '')
    preferred_language = user_prefs.get('language', 'English')
    prefers_instrumental = user_prefs.get('prefers_instrumental', False)

    def retrieve_candidates(user_prefs: Dict, songs: List[Dict]) -> List[Dict]:
        filtered = [s for s in songs if (
            (not user_prefs.get('genre') or s['genre'] == user_prefs.get('genre')) or
            (not user_prefs.get('mood') or s['mood'] == user_prefs.get('mood'))
        )]
        if not filtered:
            logging.info("No candidates after filtering, using all songs.")
            return songs
        logging.info(f"Filtered candidates: {len(filtered)}")
        return filtered

    def score_song(song: Dict) -> float:
        score = 0.0
        if song['genre'] == favorite_genre:
            score += 1.25
        if song['mood'] == favorite_mood:
            score += 1.5
        energy_diff = abs(song['energy'] - target_energy)
        if energy_diff <= 0.05:
            energy_bonus = 1.0
        elif energy_diff <= 0.15:
            energy_bonus = 0.9 - (energy_diff * 0.5)
        else:
            energy_bonus = 1.0 - (energy_diff * 3)
        score += 2 * energy_bonus
        if likes_acoustic:
            score += song['acousticness'] * 0.6
        else:
            score -= song['acousticness'] * 0.6
        score += (song.get('popularity', 50) / 100.0)
        if favorite_decade and song.get('release_decade', '') == favorite_decade:
            score += 0.5
        if favorite_detailed_mood and song.get('detailed_mood', '') == favorite_detailed_mood:
            score += 0.7
        if prefers_instrumental:
            score += song.get('instrumentalness', 0.0) * 0.5
        if preferred_language and song.get('language', 'English') == preferred_language:
            score += 0.3
        return score

    def retrieve_similar_songs(target_song: Dict, all_songs: List[Dict], top_n: int = 2) -> List[Dict]:
        similar = [s for s in all_songs if s['id'] != target_song['id'] and (
            s['genre'] == target_song['genre'] or s['mood'] == target_song['mood'] or s['artist'] == target_song['artist'])]
        def sim_score(s):
            return (
                (s['genre'] == target_song['genre']) +
                (s['mood'] == target_song['mood']) +
                (s['artist'] == target_song['artist'])
            )
        similar.sort(key=sim_score, reverse=True)
        return similar[:top_n]

    def explain_song(song: Dict, user_prefs: Dict, all_songs: List[Dict]) -> str:
        reasons = []
        if song['genre'] == user_prefs.get('genre'):
            reasons.append(f"matches your favorite genre '{user_prefs.get('genre')}'")
        if song['mood'] == user_prefs.get('mood'):
            reasons.append(f"matches your favorite mood '{user_prefs.get('mood')}'")
        energy_diff = abs(song['energy'] - user_prefs.get('energy', 0.5))
        if energy_diff < 0.1:
            reasons.append("has energy level very close to your target")
        elif energy_diff < 0.3:
            reasons.append("has energy level somewhat close to your target")
        if user_prefs.get('likes_acoustic', False) and song['acousticness'] > 0.5:
            reasons.append("is acoustic, which you prefer")
        elif not user_prefs.get('likes_acoustic', False) and song['acousticness'] < 0.3:
            reasons.append("is not very acoustic, matching your preference")
        if song.get('release_decade'):
            reasons.append(f"from the {song['release_decade']}s")
        if song.get('language'):
            reasons.append(f"in {song['language']}")
        similar = retrieve_similar_songs(song, all_songs)
        if similar:
            sim_titles = ", ".join([f"'{s['title']}' by {s['artist']}" for s in similar])
            reasons.append(f"Similar songs you might like: {sim_titles}")
        if reasons:
            return f"This song {', '.join(reasons)}."
        else:
            return "This song may not perfectly match your preferences, but give it a listen!"

    # --- Pipeline ---
    # Step 1: Filter
    candidate_songs = retrieve_candidates(user_prefs, songs)
    # Step 2: Score + rank
    scored = [(song, score_song(song)) for song in candidate_songs]
    scored.sort(key=lambda x: x[1], reverse=True)
    # Step 3: Diversity penalty
    top = []
    seen_artists = set()
    for song, score in scored:
        penalty = 0.0
        if song['artist'] in seen_artists:
            penalty = 0.7
        else:
            seen_artists.add(song['artist'])
        top.append((song, score - penalty))
        if len(top) >= k:
            break
    top.sort(key=lambda x: x[1], reverse=True)
    # Step 4: Retrieve explanations
    final = [(song, score, explain_song(song, user_prefs, songs)) for song, score in top[:k]]
    return final
