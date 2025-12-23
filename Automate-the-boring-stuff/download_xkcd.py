#! python3

# download_xkcd.py - Downloads every single XKCD comic.

import os

import bs4
import requests

url = "https://xkcd.com"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in "xkcd" folder

while not url.endswith("#"):
    # Download the page.
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the URL of the comic image.
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = comic_elem[0].get("src")
        if not comic_url.startswith("https:"):
            comic_url = f"https:{comic_url}"

        # Donwload the image.
        print(f"Downloading image {comic_url}...")
        res = requests.get(comic_url)
        res.raise_for_status()

        # Save the image to "xkcd" folder.
        image_file = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
        for chunk in res.iter_content(100000):
            image_file.write(chunk)

        image_file.close()

    # Get the Prev button's url.
    prev_link = soup.select('a[rel="prev"]')[0]
    url = f"https://xkcd.com{prev_link.get('href')}"

print("Download completed.")
