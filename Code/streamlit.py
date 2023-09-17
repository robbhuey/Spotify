import streamlit as st
import pandas as pd
import numpy as np

#Streamlit code.

# Function to recommend songs by energy
def recommend_songs_by_energy(input_energy, num_recommendations=10):
    rec['energy_difference'] = np.abs(rec['energy'] - input_energy)
    rec_sorted = rec.sort_values('energy_difference')
    top_recommendations = rec_sorted.head(num_recommendations)
    return top_recommendations

def main():
    
    st.title("Spotify Energy Recommender")
    st.subheader("Discover music based on your current energy level!")

# User input for energy
    input_energy = st.number_input("How energetic are you feeling? (between 1 and 100)", 1, 100)

# Get song recommendations based on the input energy value
    recommendations = recommend_songs_by_energy(input_energy)

# Display the top recommended songs
    st.header(f"Top {len(recommendations)} Songs for Your Current Energy Level: {input_energy}")
    st.table(recommendations[['song title', 'artist', 'energy']])

if __name__ == "__main__":
    rec = pd.read_csv('../Data/clean/rec.csv')
    main()

