#! python3

# search.py - Opens several search results.

import sys
import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

print("Searching...")
query = " ".join(sys.argv[1:])

chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment for headless mode

driver = webdriver.Chrome(options=chrome_options)

try:
    # Use DuckDuckGo - no CAPTCHA, no bot detection
    driver.get(f"https://duckduckgo.com/?q={query}")
    time.sleep(2)

    # Save page source for debugging
    # with open("files/output.txt", "w", encoding="utf-8") as so:
    #    so.write(driver.page_source)

    # Get search result links
    links = driver.find_elements(By.CSS_SELECTOR, "a[data-testid='result-title-a']")

    urls = []
    for link in links:
        href = link.get_attribute("href")
        if href and href.startswith("http"):
            urls.append(href)

    print(f"Found {len(urls)} results")

    # Open first 5 results
    for i, url in enumerate(urls[:5], 1):
        print(f"{i}. {url}")
        webbrowser.open(url)
        time.sleep(1)

except Exception as e:
    print(f"Error: {e}")
    # print("Check files/output.txt for debug info")

finally:
    driver.quit()
