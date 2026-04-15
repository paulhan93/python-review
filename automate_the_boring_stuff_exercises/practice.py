# script: solution.py

import sys
import re
import requests
from bs4 import BeautifulSoup


def decode_secret_message(url: str):
    # fetch the document as HTML
    response = requests.get(url)
    response.raise_for_status()

    # parse the table
    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table")
    if not table:
        raise ValueError("No table found in document")

    # extract table from google doc into data (list of tuples for each entry)
    rows = table.find_all("tr")
    data = []
    for row in rows[1:]:  # skip header row
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        x = int(cells[0].get_text(strip=True))
        char = cells[1].get_text(strip=True)
        y = int(cells[2].get_text(strip=True))
        data.append((x, y, char))

    if not data:
        raise ValueError("No data parsed from table")

    # determine the grid size
    max_x = max(x for x, y, c in data)
    max_y = max(y for x, y, c in data)

    # build the grid (filled with spaces for now)
    grid = [[" "] * (max_x + 1) for _ in range(max_y + 1)]

    # fill the grid with each entry:
    for x, y, char in data:
        grid[y][x] = char

    # print the grid
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    if (len(sys.argv)) != 2:
        print("Usage: python solution.py <URL>")
        sys.exit(1)
    decode_secret_message(sys.argv[1])
