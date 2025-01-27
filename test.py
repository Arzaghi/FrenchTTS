import os
import pytest
from main import read_text_file, text_to_speech, input_directory, output_directory

@pytest.fixture(scope="module")
def setup_directories():
    if not os.path.exists(input_directory):
        os.makedirs(input_directory)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    yield
    for file_name in ["test_input.txt", "test_output.mp3"]:
        file_path = os.path.join(input_directory if file_name.endswith(".txt") else output_directory, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)

def test_read_text_file(setup_directories):
    input_file = os.path.join(input_directory, 'test_input.txt')
    with open(input_file, 'w', encoding='utf-8') as file:
        file.write('Bonjour.\nComment ça va?\nBienvenue!\n')
    
    expected = ['Bonjour.', 'Comment ça va?', 'Bienvenue!']
    result = read_text_file(input_file)
    assert result == expected

def test_text_to_speech(setup_directories):
    text_lines = ['Bonjour.', 'Comment ça va?', 'Bienvenue!']
    output_file = os.path.join(output_directory, 'test_output.mp3')
    text_to_speech(text_lines, output_file)
    assert os.path.exists(output_file)
