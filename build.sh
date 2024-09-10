#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Build the executable
pyinstaller --name="YoutubeDownloaderByPaulPham157" --windowed --onefile app.py

echo "Build completed. The executable is in the 'dist' folder."