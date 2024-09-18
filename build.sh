#!/bin/bash
if [ "$1" = "--clean" ]; then
    rm -rf build dist *.spec *.egg-info
    conda activate yt-dlp
    pip freeze > requirements.txt
    pip uninstall -y -r requirements.txt
    rm requirements.txt
    pip install -e .
fi

if [ ! -d "src/vendors/ffmpeg" ]; then
    echo "Đang tạo thư mục src/vendors/ffmpeg..."
    mkdir -p src/vendors/ffmpeg
    echo "Đã tạo xong thư mục src/vendors/ffmpeg"
else
    echo "Thư mục src/vendors/ffmpeg đã tồn tại"
fi

if [ ! -f "src/vendors/ffmpeg/ffmpeg" ]; then
    echo "Đang tải ffmpeg linux..."
    curl -L https://evermeet.cx/ffmpeg/ffmpeg-7.0.2.zip -o ffmpeg-linux.zip
    unzip ffmpeg-linux.zip
    rm ffmpeg-linux.zip
    mv ffmpeg src/vendors/ffmpeg/
    rm ffmpeg
    echo "Đã tải xong ffmpeg linux"
elif [ ! -f "src/vendors/ffmpeg/ffmpeg.exe" ]; then
    echo "Đang tải ffmpeg windows..."
    curl -L https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip -o ffmpeg-windows.zip
    unzip ffmpeg-windows.zip
    rm ffmpeg-windows.zip
    mv ffmpeg-*-essentials_build/bin/ffmpeg.exe ffmpeg-*-essentials_build/bin/ffplay.exe ffmpeg-*-essentials_build/bin/ffprobe.exe src/vendors/ffmpeg/
    rm -rf ffmpeg-*-essentials_build
    echo "Đã tải xong ffmpeg windows"
else
    echo "Phần phụ thuộc ffmpeg đã tồn tại, bỏ qua bước tải ffmpeg"
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
    OS="macos"
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    OS="windows"
else
    echo "Hệ điều hành không được hỗ trợ"
    exit 1
fi

build_macos() {
    echo "Đang build cho macOS..."
    pyinstaller --name="macOS-DiuTupDownloaderByPaulPham157" \
                --icon 'src/assets/images/DiuTupDownloaderByPaulPham157.icns' \
                --windowed \
                --onefile \
                --noconfirm \
                --add-data "src/vendors/ffmpeg/ffmpeg:src/vendors/ffmpeg/ffmpeg" \
                --add-data "src/assets/images:src/assets/images" \
                src/app.py
    if [ -d "dist/macOS-DiuTupDownloaderByPaulPham157.app" ]; then
        echo "Đang nén file macOS..."
        version=$(grep -E '^version\s*=' pyproject.toml | awk -F'"' '{print $2}')
        zip_name="macos-dtdbpp157_v-${version}.zip"
        (cd dist && zip -r "$zip_name" "macOS-DiuTupDownloaderByPaulPham157.app" && cp -av $zip_name ~/Downloads/)
        echo "Đã tạo file nén: $zip_name"
    else
        echo "Không tìm thấy thư mục dist/macOS-DiuTupDownloaderByPaulPham157.app"
    fi
}

build_windows() {
    echo "Đang build cho Windows..."
    pyinstaller --name="Windows-DiuTupDownloaderByPaulPham157" \
                --icon 'src/assets/images/DiuTupDownloaderByPaulPham157.ico' \
                --windowed \
                --onefile \
                --noconfirm \
                --add-data "src/vendors/ffmpeg/ffmpeg.exe:src/vendors/ffmpeg/ffmpeg.exe" \
                --add-data "src/vendors/ffmpeg/ffplay.exe:src/vendors/ffmpeg/ffplay.exe" \
                --add-data "src/vendors/ffmpeg/ffprobe.exe:src/vendors/ffmpeg/ffprobe.exe" \
                --add-data "src/assets/images:src/assets/images" \
                src/app.py
    if [ -f "dist/Windows-DiuTupDownloaderByPaulPham157" ]; then
        echo "Đang nén file Windows..."
        version=$(grep -E '^version\s*=' pyproject.toml | awk -F'"' '{print $2}')
        zip_name="windows-dtdbpp157_v-${version}.zip"
        (cd dist && zip -r "$zip_name" "Windows-DiuTupDownloaderByPaulPham157.exe" && cp -av $zip_name ~/Downloads/)
        echo "Đã tạo file nén: $zip_name"
    else
        echo "Không tìm thấy file dist/Windows-DiuTupDownloaderByPaulPham157.exe"
    fi
}

wine_build_windows() {
    echo "Cài đặt Wine..."
    if ! command -v wine &> /dev/null
    then
        echo "Wine chưa được cài đặt. Đang cài đặt Wine..."
        if ! command -v brew &> /dev/null
        then
            echo "Homebrew chưa được cài đặt. Vui lòng cài đặt Homebrew trước."
            exit 1
        else
            brew install --cask wine-stable
        fi
    else
        echo "Wine đã được cài đặt."
    fi
    echo "Đang build cho Windows trên môi trường Wine..."
    wine pyinstaller --name="Windows-DiuTupDownloaderByPaulPham157" \
                --icon 'src/assets/images/DiuTupDownloaderByPaulPham157.ico' \
                --windowed \
                --onefile \
                --noconfirm \
                --add-data "src/vendors/ffmpeg/ffmpeg.exe:src/vendors/ffmpeg/ffmpeg.exe" \
                --add-data "src/vendors/ffmpeg/ffplay.exe:src/vendors/ffmpeg/ffplay.exe" \
                --add-data "src/vendors/ffmpeg/ffprobe.exe:src/vendors/ffmpeg/ffprobe.exe" \
                --add-data "src/assets/images:src/assets/images" \
                src/app.py
    if [ -f "dist/Windows-DiuTupDownloaderByPaulPham157" ]; then
        echo "Đang nén file Windows..."
        version=$(grep -E '^version\s*=' pyproject.toml | awk -F'"' '{print $2}')
        zip_name="windows-dtdbpp157_v-${version}.zip"
        (cd dist && zip -r "$zip_name" "Windows-DiuTupDownloaderByPaulPham157.exe" && cp -av $zip_name ~/Downloads/)
        echo "Đã tạo file nén: $zip_name"
    else
        echo "Không tìm thấy file dist/Windows-DiuTupDownloaderByPaulPham157.exe"
    fi
}

if [ "$OS" == "macos" ]; then
    build_macos
elif [ "$OS" == "windows" ]; then
    build_windows
fi
