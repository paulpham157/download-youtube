#!/bin/bash

# Install requirements
pip install -r requirements.txt

# Download ffmpeg
if [ ! -f "ffmpeg" ]; then
    echo "Đang tải ffmpeg..."
    curl -L https://evermeet.cx/ffmpeg/ffmpeg-6.0.zip -o ffmpeg.zip
    unzip ffmpeg.zip
    rm ffmpeg.zip
    echo "Đã tải xong ffmpeg"
else
    echo "ffmpeg đã tồn tại, bỏ qua bước tải"
fi

# Build the executable
# v1
pyinstaller --name="YoutubeDownloaderByPaulPham157" --icon 'app.ico' --windowed --onefile --add-data "ffmpeg:." app.py
# v2
# pyinstaller app.spec

echo "Build completed. The executable is in the 'dist' folder."