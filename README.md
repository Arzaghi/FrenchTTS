# Text-to-Speech Application

This application reads all text files in the input directory and generates output MP3 files in the output directory. It adds a 3-second pause after each line of text.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

### 1. Clone the repository

```bash
git clone <repository_url>
cd <repository_name>
```

### 2. Install required libraries

```bash
pip install -r requirements.txt
```

### 3. Install ffmpeg

#### Windows

Install ffmpeg using `winget`:

```bash
winget install -e --id Gyan.FFmpeg
or
winget install ffmpeg
```

#### Linux

Install ffmpeg using your package manager:

```bash
sudo apt-get install ffmpeg
```

## Usage

1. Run the program:

   ```bash
   python main.py file1.txt file2.txt
   ```

The program will read all text files in the `input_directory` and generate MP3 files in the `output_directory`, adding a 3-second pause after each line.

## Running Tests

We use `pytest` for testing.

1. Install pytest if you haven't already:

   ```bash
   pip install pytest
   ```

2. Run the tests:

   ```bash
   pytest -p no:warnings
   ```

## Directory Structure

```plaintext
.
├── main.py
├── requirements.txt
└── test_tts_app.py
```

- `main.py`: Main application script.
- `requirements.txt`: List of required Python libraries.
- `test_tts_app.py`: Test script for the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---
