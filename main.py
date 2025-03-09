import os
import io
import argparse
from gtts import gTTS
from pydub import AudioSegment
from tqdm import tqdm

pause_time = 250

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
            combined += AudioSegment.silent(duration=pause_time)
        progress_bar.update(1)

    combined.export(output_file, format="mp3")

def process_file(input_file):
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    if not input_file.endswith(".txt"):
        print(f"Error: Input file '{input_file}' is not a text file.")
        return

    output_file = input_file.replace(".txt", ".mp3")

    text_lines = read_text_file(input_file)
    total_lines = len(text_lines)

    with tqdm(total=total_lines, desc=f"Processing {input_file}") as progress_bar:
        text_to_speech(text_lines, output_file, progress_bar)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert text files to speech.")
    parser.add_argument("input_files", type=str, nargs='+', help="Paths to the input text files.")
    args = parser.parse_args()

    for input_file in args.input_files:
        process_file(input_file)