"""
Parse Data from Merriam-Webster
"""

import os
from bs4 import BeautifulSoup
from requests_html import HTMLSession

os.makedirs("./word_list", exist_ok=True)

letters = (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', 'bio', 'geo'
)

for letter in letters:
    PAGE = 1
    list_words = []

    while True:
        url = f"https://www.merriam-webster.com/browse/dictionary/{letter}/{PAGE}"
        session = HTMLSession()
        response = session.get(url)
        print(f"Parsing: {response.html.url}")

        soup = BeautifulSoup(response.html.html, 'html.parser')

        words = soup.select("div.mw-grid-table-list a")

        for word in words:
            href = word.get("href", "")
            if href:
                list_words.append(href.split("/")[-1])

        next_disabled = soup.select(".next.disabled")

        if next_disabled:
            with open(f"./word_list/{letter}.txt", 'w', encoding="utf-8") as text_file:
                unique_words = list(dict.fromkeys(list_words))
                for word in unique_words:
                    text_file.write(word + '\n')
            break

        PAGE += 1
