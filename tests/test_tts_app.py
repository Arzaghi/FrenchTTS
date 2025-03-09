import os
import pytest
from ..main import read_text_file, text_to_speech, process_file

input_directory = "input"
output_directory = "output"

@pytest.fixture(scope="module")
def setup_directories():
    # Create input and output directories
    os.makedirs(input_directory, exist_ok=True)
    os.makedirs(output_directory, exist_ok=True)
    yield
    # Clean up: remove created directories and files
    for file in os.listdir(input_directory):
        os.remove(os.path.join(input_directory, file))
    for file in os.listdir(output_directory):
        os.remove(os.path.join(output_directory, file))
    os.rmdir(input_directory)
    os.rmdir(output_directory)

def test_read_text_file(setup_directories):
    sample_text = "Hello\nWorld\n"
    sample_file_path = os.path.join(input_directory, "sample.txt")
    with open(sample_file_path, "w", encoding="utf-8") as file:
        file.write(sample_text)

    lines = read_text_file(sample_file_path)
    assert lines == ["Hello", "World"]

def test_text_to_speech(setup_directories):
    text_lines = ["Hello", "World"]
    output_file = os.path.join(output_directory, "output.mp3")

    from tqdm import tqdm
    with tqdm(total=len(text_lines), desc="Testing text_to_speech") as progress_bar:
        text_to_speech(text_lines, output_file, progress_bar)

    assert os.path.exists(output_file)

def test_process_file(setup_directories):
    sample_text = "Hello\nWorld\n"
    sample_file_path = os.path.join(input_directory, "sample.txt")
    output_file_path = os.path.join(input_directory, "sample.mp3")
    with open(sample_file_path, "w", encoding="utf-8") as file:
        file.write(sample_text)

    process_file(sample_file_path)

    assert os.path.exists(output_file_path)