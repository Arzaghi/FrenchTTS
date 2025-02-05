import os
import io
from gtts import gTTS
from pydub import AudioSegment
from tqdm import tqdm

input_directory = "input"
output_directory = "output"

def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def text_to_speech(text_lines, output_file, progress_bar):
    combined = AudioSegment.empty()
    temp_file = "temp.mp3"
    for line in text_lines:
        if line:
            tts = gTTS(text=line, lang='fr')        
            tts.save(temp_file)
            sound = AudioSegment.from_mp3(temp_file)
            combined += sound
            combined += AudioSegment.silent(duration=3000)  # Add 3-second pause
        progress_bar.update(1)

    combined.export(output_file, format="mp3")

def process_files():
    if not os.path.exists(input_directory):
        print(f"Error: Input directory '{input_directory}' does not exist.")
        return

    text_files = [f for f in os.listdir(input_directory) if f.endswith(".txt")]
    if not text_files:
        print(f"Error: No new text files found in the input directory '{input_directory}'.")
        return

    total_lines = sum(len(read_text_file(os.path.join(input_directory, f))) for f in text_files)

    with tqdm(total=total_lines, desc="Processing all lines") as progress_bar:
        for file_name in text_files:
            input_file = os.path.join(input_directory, file_name)
            output_file = os.path.join(output_directory, file_name.replace(".txt", ".mp3"))

            text_lines = read_text_file(input_file)
            text_to_speech(text_lines, output_file, progress_bar)

if __name__ == "__main__":
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    process_files()
