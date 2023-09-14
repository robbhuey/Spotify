import streamlit as st
import pandas as pd
import numpy as np

background_image_style = """
<style>
body {
    background-image: url("https://duet-cdn.vox-cdn.com/thumbor/0x0:2040x1360/640x427/filters:focal(1020x680:1021x681):format(webp)/cdn. vox-cdn.com/uploads/chorus_asset/file/22026912/acastro_201110_4286_spotify_0001.jpg");
    background-size: cover;
}
</style>
"""
# Display the custom CSS in the Streamlit app
st.markdown(background_image_style, unsafe_allow_html=True)

# Function to recommend songs by energy
def recommend_songs_by_energy(input_energy, num_recommendations=10):
    rec['energy'] = rec['energy'] / 100
    rec['energy_difference'] = np.abs(rec['energy'] - (input_energy / 100))
    rec_sorted = rec.sort_values('energy_difference')
    top_recommendations = rec_sorted.head(num_recommendations)
    return top_recommendations

def main():
    st.title("Song Recommendation by Energy")

    # Input your desired energy value (between 1 and 100)
    input_energy = st.number_input("Please enter the energy value: ")

    # Get song recommendations based on the input energy value
    recommendations = recommend_songs_by_energy(input_energy)
    recommendations['energy'] = recommendations['energy'] * 100

    # Display the top recommended songs
    st.header(f"Top {len(recommendations)} Recommended Songs for Energy Near {input_energy}:")
    st.table(recommendations[['song title', 'artist', 'energy']])
    
if __name__ == "__main__":
    rec = pd.read_csv('rec.csv')
    main()

