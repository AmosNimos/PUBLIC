from gtts import gTTS
from playsound import playsound

file_name = str(input("File:"))
def load_file(file_name:str):
    with open(file_name+".txt") as f:
        file_text = f.read()
		
        return file_text

file_text = load_file(file_name)

# make request to google to get synthesis
tts = gTTS(file_text)
# save the audio file
tts.save(file_name+".mp3")
# play the audio file
playsound(file_name+".mp3")
