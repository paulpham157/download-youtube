#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Build the executable
pyinstaller --name="Download playlist YT as audio files" --windowed --onefile app.py

echo "Build completed. The executable is in the 'dist' folder."