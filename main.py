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
    for line in text_lines:
        tts = gTTS(text=line, lang='fr')
        with io.BytesIO() as temp_audio:
            tts.write_to_fp(temp_audio)
            temp_audio.seek(0)
            sound = AudioSegment.from_file(temp_audio, format="mp3")
            combined += sound
            combined += AudioSegment.silent(duration=3000)  # Add 3-second pause
        progress_bar.update(1)

    combined.export(output_file, format="mp3")

def process_files():
    text_files = [f for f in os.listdir(input_directory) if f.endswith(".txt")]
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
