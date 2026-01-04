#! python3

# multi_download_xkcd.py - Downloads XKCD comics using multiple threads.

import os
import threading

import bs4
import requests

url = "https://xkcd.com"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in "xkcd" folder


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print(f"Downloading page {url}/{url_number}")
        res = requests.get(f"{url}/{url_number}")
        try:
            res.raise_for_status()

            soup = bs4.BeautifulSoup(res.text, "lxml")

            # Find the url of the comic image.
            comic_elem = soup.select("#comic img")
            if comic_elem == []:
                print("Could not find the comic image.")
            else:
                comic_url = comic_elem[0].get("src")
                if not comic_url.startswith("https:"):
                    comic_url = f"https:{comic_url}"

                # Download the image.
                print(f"Downloading image {comic_url}...")
                res = requests.get(comic_url)
                res.raise_for_status()

                # Save the image to "xkcd" folder.
                with open(
                    os.path.join("xkcd", os.path.basename(comic_url)), "wb"
                ) as image_file:
                    for chunk in res.iter_content(100000):
                        image_file.write(chunk)
        except requests.exceptions.HTTPError as e:
            print(f"Skipping comic {url_number}: {e}")
            continue


# Create and start the Thread objects.
download_threads = []  # a list of all the Thread objects
for i in range(1, 1400, 100):  # loops 14 times, creates 14 threads
    download_thread = threading.Thread(target=download_xkcd, args=(i, i + 99))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for download_thread in download_threads:
    download_thread.join()

print("Donwload completed.")
