from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

channel = "https://www.youtube.com/playlist?list=PLT1rvk7Trkw4Y-8LJ0-yw_fOqHhij6ssA"


def get_shorts_links(channel):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(channel)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    driver.execute_script(
        """
        var scroll = setInterval(function(){
            window.scrollBy(0, 1000);
        }, 1000);
    """
    )
    updated_page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(updated_page_source, "html.parser")
    video_tags = soup.find_all(
        "a",
        {
            "class": "reel-item-endpoint",
        },
    )
    shorts = []
    for video_tag in video_tags:
        href = video_tag.get("href", "N/A")
        if "shorts" in href:
            video_url = "https://www.youtube.com" + href
            shorts.append(video_url)
    return shorts


print(get_shorts_links(channel))
