# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name

**VibeFinder 1.0**

---

## 2. Intended Use

This recommender suggests songs based on your mood, favorite genre, and energy level. It is designed for classroom learning and exploring how music recommenders work. It is not meant for real-world music streaming or commercial use.

---

## 3. How the Model Works

The model looks at your favorite genre, mood, and how much energy you want in a song. It scores each song higher if it matches your genre or mood, and if its energy is close to your target. It also considers if you like acoustic music. The top scoring songs are recommended to you. The scoring rules are simple and use only a few features.

---

## 4. Data

The dataset has 20 songs. Each song has features like genre, mood, energy, tempo, valence, danceability, and acousticness. There are many genres, but some (like pop and lofi) appear more often. No data was added or removed. Some musical styles and moods are missing, so not every taste is covered.

---

## 5. Strengths

The system works well for users who like popular genres and common moods. It gives good results when your preferences match the songs in the dataset. The recommendations make sense for typical cases, like happy pop or chill lofi fans.

---

## 6. Limitations and Bias

Where the system struggles or behaves unfairly.

Prompts:

- Features it does not consider
- Genres or moods that are underrepresented
- Cases where the system overfits to one preference
- Ways the scoring might unintentionally favor some users

One weakness discovered during testing is that the system can over-prioritize certain genres, such as pop or rock, if they are more common in the dataset. Users whose favorite genre or mood is not present in the data will rarely receive high-scoring recommendations, regardless of their other preferences. The current scoring logic also heavily rewards close matches on energy, which can create a filter bubble and limit variety for users with extreme or uncommon energy preferences. Additionally, features like valence, danceability, and tempo are ignored, so users with strong preferences for these attributes are not well-served. These factors can lead to biased recommendations and reduced diversity in the results.

---

## 7. Evaluation

How you checked whether the recommender behaved as expected.

Prompts:

- Which user profiles you tested
- What you looked for in the recommendations
- What surprised you
- Any simple tests or comparisons you ran

For evaluation, I tested a variety of user profiles, including typical cases (e.g., pop/happy/high energy) and adversarial or edge cases (such as high energy with sad mood, or genres/moods not present in the dataset). I looked for whether the top recommendations matched the user's stated preferences and if the same songs appeared repeatedly. One surprise was how strongly the system favored songs that matched genre and energy, sometimes at the expense of mood or other features. For users with rare or conflicting preferences, the recommendations were often less relevant or repetitive, highlighting the system's sensitivity to dataset composition and scoring weights.

No need for numeric metrics unless you created some.

---

## 8. Future Work

I would add more features, like danceability and tempo, to make recommendations smarter. I would also try to make the results more diverse, so you see new songs sometimes. Finally, I would improve the explanations so users know why a song was picked.

---

## 9. Personal Reflection

I learned that recommenders can be simple but still show patterns and biases. It was interesting to see how changing the weights or the data changed the results. This project made me think more about how music apps decide what to play next!

## 10. Intended Use and Non-Intended Use

This system is for learning and experimenting with music recommendation. It should not be used for real music streaming, commercial products, or making important decisions.
