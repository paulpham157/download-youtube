#!/bin/bash

# # Install requirements
# pip install -r requirements.txt

# # Download ffmpeg
# if [ ! -f "ffmpeg" ]; then
#     echo "Đang tải ffmpeg..."
#     curl -L https://evermeet.cx/ffmpeg/ffmpeg-7.0.2.zip -o ffmpeg.zip
#     unzip ffmpeg.zip
#     rm ffmpeg.zip
#     echo "Đã tải xong ffmpeg"
# else
#     echo "ffmpeg đã tồn tại, bỏ qua bước tải"
# fi

# Build the executable
# v1
pyinstaller --name="DiuTupDownloaderByPaulPham157" --icon 'src/assets/images/DiuTupDownloaderByPaulPham157.icns' --windowed --onefile --noconfirm --add-data "src/vendors/ffmpeg/ffmpeg:./src/vendors/ffmpeg/ffmpeg" src/app.py
# v2
# pyinstaller DiuTupDownloaderByPaulPham157.spec

echo "Build completed. The executable is in the 'dist' folder."