import csv
import logging
import os
import requests as req
from bs4 import BeautifulSoup

# Prepare logging
log_folder = "scrapping/logs"
os.makedirs(log_folder, exist_ok=True)
log_file = os.path.join(log_folder, "log.txt")

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

try:
    # Target URL
    url = "https://beallslist.net/standalone-journals/"
    response = req.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Prepare output data folder
    output_folder = "scrapping/data"
    os.makedirs(output_folder, exist_ok=True)

    # File PATH
    csv_file_path = os.path.join(output_folder, 'predatory_journal.csv')

    # Target Element
    ul_tags = soup.find_all('ul')

    journal_data = []
    for ul in ul_tags:
        li_items = ul.find_all('li')
        for li in li_items:
            name = li.get_text(strip=True)
            link_tag = li.find('a')
            link = link_tag['href'] if link_tag else ''
            journal_data.append([name, link])

    logging.info(f'Successfully fetched url: {url}')
    
except req.RequestException as e:
    logging.error(f'Failed to fetch url: {url} error: {e}')
    raise SystemExit(e)

try:
    # Write to CSV
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Link'])
        writer.writerows(journal_data)
        
except Exception as e:
    logging.error(f"Failed to write CSV - Error: {e}")
    raise SystemExit(e)

