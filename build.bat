@echo off

REM Install requirements
pip install -r requirements.txt

REM Download ffmpeg
if not exist ffmpeg.exe (
    echo Dang tai ffmpeg...
    powershell -Command "Invoke-WebRequest -Uri 'https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip' -OutFile 'ffmpeg.zip'"
    powershell -Command "Expand-Archive -Path 'ffmpeg.zip' -DestinationPath 'ffmpeg_temp' -Force"
    move ffmpeg_temp\ffmpeg-*-essentials_build\bin\ffmpeg.exe .
    rmdir /s /q ffmpeg_temp
    del ffmpeg.zip
    echo Da tai xong ffmpeg
) else (
    echo ffmpeg da ton tai, bo qua buoc tai
)

REM Build the executable
pyinstaller --name="DiuTupDownloaderByPaulPham157" --windowed --onefile --add-data "ffmpeg.exe;." app.py

echo Build completed. The executable is in the 'dist' folder.