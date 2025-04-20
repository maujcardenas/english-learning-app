import streamlit as st
import pandas as pd
import os
import tools.utils as ut  # Assuming this is your custom utility module

# Load the dataframe
df = ut.load_working_vocab_df()

# Create the main title
st.title("Vocabulary Explorer")

# Create category selector
categories = df['category'].unique()
selected_category = st.selectbox("Select Category", categories)

# Filter subcategories based on selected category
subcategories = df[df['category'] == selected_category]['sub-category'].unique()
selected_subcategory = st.selectbox("Select Subcategory", subcategories)

# Filter the dataframe based on selections
filtered_df = df[
    (df['category'] == selected_category) & 
    (df['sub-category'] == selected_subcategory)
]

# Display the filtered dataframe without category and sub-category columns
display_df = filtered_df[['word', 'type', 'example']]
st.dataframe(display_df, hide_index=True, use_container_width=False)

# Display each word with its details and audio
st.markdown("---")
st.header("Words in Detail")

for index, row in filtered_df.iterrows():

    word=row['word'].strip()
    example_sentence=row['example'].strip()
    
    
    # Construct audio file paths
    word_audio_path = os.path.join("english_audio", f"{row['sub-category'].strip()}-{row['word'].strip()}") + '.mp3'


    example_audio_path = os.path.join("english_audio", f"{row['sub-category'].strip()}-{row['word'].strip()}-example")+'.mp3'

    # Display audio players
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'#### {word}')
        if os.path.exists(word_audio_path):
            st.audio(word_audio_path)
        else:
            st.warning("Word audio file not found")
    
    with col2:
        st.markdown(f'#### {example_sentence}')
        if os.path.exists(example_audio_path):
            st.audio(example_audio_path)
        else:
            st.warning("Example audio file not found")
    
    st.markdown("---")

# Optional: Add some styling or additional information at the bottom
st.markdown("### Notes")
st.info("Select a category and subcategory to view vocabulary words with their examples and audio recordings.")