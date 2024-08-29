from gtts import gTTS
import os

text = "Hello, this is a test of text to speech conversion."
tts = gTTS(text=text, lang='en')
tts.save("output.mp3")

# Optionally, you can play the saved file
os.system("start output.mp3")  # On Windows
# os.system("afplay output.mp3")  # On macOS
# os.system("mpg321 output.mp3")  # On Linux