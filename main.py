import os
from gtts import gTTS
from pydub import AudioSegment

input_directory = "input"
output_directory = "output"

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def text_to_speech(text_lines, output_file):
    combined = AudioSegment.empty()
    temp_file = "temp.mp3"
    for line in text_lines:
        tts = gTTS(text=line, lang='fr')        
        tts.save(temp_file)
        sound = AudioSegment.from_mp3(temp_file)
        combined += sound
        combined += AudioSegment.silent(duration=3000)  # Add 3-second pause

    os.remove(temp_file)

    combined.export(output_file, format="mp3")
    print(f"MP3 file saved as: {output_file}")

def process_files():
    for file_name in os.listdir(input_directory):
        if file_name.endswith(".txt"):
            input_file = os.path.join(input_directory, file_name)
            output_file = os.path.join(output_directory, file_name.replace(".txt", ".mp3"))

            text_lines = read_text_file(input_file)
            text_to_speech(text_lines, output_file)

if __name__ == "__main__":
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    process_files()
