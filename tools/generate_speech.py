import pandas as pd
import os
import re
from gtts import gTTS
import time
import csv


# Function to sanitize filenames
def sanitize_filename(filename):
    # Replace invalid filename characters with underscores
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

# Create output directory if it doesn't exist
output_dir = "english_audio"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Read the CSV file
df = pd.read_csv("english-vocab.csv", sep=',', encoding="utf-8", engine='python', quotechar='"', doublequote=True)
 
# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Process each row in the dataframe
for index, row in df.iterrows():
    try:
        # Extract data from the CSV
        subcategory = sanitize_filename(row['sub-category'].strip())
        word = sanitize_filename(row['word'].strip())
        # Remove quotes from example if they exist
        example = row['example'].strip()
        if example.startswith('"') and example.endswith('"'):
            example = example[1:-1].strip()
        
        # Create filenames with sanitized names
        word_filename = f"{output_dir}/{subcategory}-{word}.mp3"
        example_filename = f"{output_dir}/{subcategory}-{word}-example.mp3"
        
        # Generate word audio
        print(f"Generating audio for word: {row['word']}")
        word_tts = gTTS(row['word'], lang='en')
        word_tts.save(word_filename)
        
        # Generate example sentence audio
        print(f"Generating audio for example: {example}")
        example_tts = gTTS(example, lang='en')
        example_tts.save(example_filename)
        
        # Add delay to avoid hitting Google's rate limits
        time.sleep(1)
        
        # Print progress
        print(f"Processed {index+1}/{len(df)} entries.")
        
    except Exception as e:
        print(f"Error processing entry {index+1}: {str(e)}")
        print(f"Skipping to next entry...")
        continue

print("Audio generation complete!")