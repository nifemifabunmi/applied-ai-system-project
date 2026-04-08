# Reflection: Comparing User Profiles and Recommendations

- Comparing the 'pop, happy, high energy' profile to the 'lofi, chill, low energy' profile, I noticed that the pop profile consistently recommends upbeat, energetic songs like 'Sunrise City' and 'Gym Hero.' This makes sense because these songs match both the genre and energy preferences. In contrast, the lofi profile shifts toward slower, more relaxed tracks with higher acousticness, such as 'Midnight Coding' and 'Library Rain.'

- When testing a 'rock, intense, high energy' profile versus a 'blues, sad, high energy' profile, the rock profile surfaces songs like 'Storm Runner' that fit the intense mood and high energy, while the blues profile struggles to find perfect matches and often recommends songs that only partially fit the criteria. This shows that the system is more effective when the user's preferences align with the dataset.

- I also observed that 'Gym Hero' appears frequently for users who want 'Happy Pop.' This is because the song's genre and energy closely match those preferences, and the scoring logic heavily rewards those features. As a result, the same songs can dominate recommendations for similar profiles, especially when the dataset is small or lacks diversity.

- Overall, the differences in recommendations between profiles make sense given the scoring logic, but also highlight the importance of dataset variety and balanced weighting of features.
