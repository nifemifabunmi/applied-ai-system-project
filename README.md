# 🎵 Music Recommender Simulation
```markdown
# 🎧 Model Card - Music Recommender Simulation

## Project Summary

This project is a simple music recommender that suggests songs based on a user's taste profile. It uses features like genre, mood, energy, and other song attributes to score and rank songs.

The goal of this project is to:

- represent songs and user preferences as data
- build a scoring system for recommendations
- test how changes affect results
- reflect on bias and limitations in recommender systems

---

## How The System Works

This recommender uses a **content-based filtering** approach. Instead of using listening history from many users, it compares the features of each song to a user’s taste profile.

Each song includes features like:

- genre
- mood
- energy
- tempo
- valence
- danceability
- acousticness
- popularity
- release decade
- language

The system creates a user profile based on liked songs and compares each song to that profile. Songs that are more similar get higher scores and are ranked as better recommendations.

---


### Algorithm Recipe
The recommender scores songs by comparing them to the user’s preferences.

- Numerical features like **energy** and **valence** are scored by how close they are to the user’s target values
- Matching **genre** and **mood** adds bonus points
- Songs are ranked by total score and the top matches are recommended

This makes the system easy to understand and experiment with.

---


### Potential Biases
Some possible biases in this recommender include:

- over-prioritizing certain genres
- recommending similar songs too often
- limited variety because of the small dataset
- struggling with unusual or mixed preferences

---


## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

I tested a few changes to see how the recommender responded.

- Lowering the genre weight made the recommendations less repetitive and allowed more variety
- Adding features like popularity, release decade, and detailed mood made the results feel more personalized
- Adding a diversity penalty helped reduce repeated artists in the top recommendations
- Changing the importance of energy and genre showed that even small weight changes can noticeably affect rankings

Here are some of the sreenshots:
- https://vscode.dev/github/nifemifabunmi/ai110-module3show-musicrecommendersimulation-starter/blob/main/Screenshot%202026-04-07%20at%207.37.23%E2%80%AFPM.png
- 

These experiments showed that recommendation systems are very sensitive to feature design and scoring choices.

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

This recommender has a few important limitations:

- it only works on a small song dataset
- it does not understand lyrics or deeper meaning
- it may over-favor certain genres or moods
- it may not work well for niche or conflicting preferences

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this

This project helped me understand how recommender systems turn data into ranked predictions. I learned that even a simple scoring system can feel personalized, but it also depends heavily on the dataset and feature weights.

One of the biggest lessons was that bias can appear easily. Small choices in data or scoring can shape what gets recommended and what gets ignored. This made me think more critically about how real-world music recommenders influence what people discover.

---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  