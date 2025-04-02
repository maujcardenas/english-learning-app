import pyttsx3

def generate_speech_file(text, rate=150, filename="output.mp3"):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    # Save to file instead of playing directly
    engine.save_to_file(text, filename)
    engine.runAndWait()
    
    return filename