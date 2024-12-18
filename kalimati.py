import csv
import requests
from bs4 import BeautifulSoup

cookies = {
    '_gid': 'GA1.3.1198343799.1734450784',
    'XSRF-TOKEN': 'eyJpdiI6IlQvOVZJamVkLzlHQ0ZkTFRKSFVTS3c9PSIsInZhbHVlIjoibGFQS0tYenNhcnczRVpFZTE2Sjc4eWE2QjhFekYzaUxnRzNPZWZLZUNBV00wZ2pHNlg5Smx6dEI2YVVBQnpxTytwUS8ySk5DVWc1eUZBRmpJN1psS29JZ3dadnFHcHVONXZxUjVGOVdhQ2Z3SnJIZFJvQXR2VHNTTHFhazM5TEsiLCJtYWMiOiI3MjRmN2QzNTM5ZDk4Mzc0OTVmN2YxZjlhMjJkMDMwNzY0OGQ4ZDM4ZjQwNjRjYWRkZDMzZmNlM2Y4NTM2ODcwIiwidGFnIjoiIn0%3D',
    'kalimati_fruits_and_vegetable_market_development_board_session': 'eyJpdiI6InVhaW5LK0MvcXZvdzhlOTR6N3NDK3c9PSIsInZhbHVlIjoibkp2RWpNa3VjUWNuUk9oMkxDV2pUU01yQ1pHdHF2WitYRzA3YW40ZGU5dUxvbWt2bURvSmVhTFNBWXpwdDFUQjkzc3lmTHlya1RGUVkzRHZMTHVhT0swSmk3dTVMdUhWOGlvb2pNb25rT0FyRlU4R0VuMWVrMTFZVU9jdEZMWHkiLCJtYWMiOiI0YTI5MmNlNDFkMTliMDM1OTQzMjcyNjA3OTVjZjk3ZTA3Y2FhODBhZWJhZmFkZDQ5YjIxNzM3MTg3NWJhNDJhIiwidGFnIjoiIn0%3D',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-IN,en-US;q=0.9,en-GB;q=0.8,en;q=0.7',
    'priority': 'u=0, i',
    'referer': 'https://kalimatimarket.gov.np/comparative-prices',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

response = requests.get('https://kalimatimarket.gov.np/price', cookies=cookies, headers=headers)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table')

# Open the CSV file for writing inside the 'with open()' block
with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    if table:
        headers = table.find('thead')
        if headers:
            headers_row = headers.find('tr')
            header_columns = headers_row.find_all('th')
            # Write header row to the CSV inside the 'with' block
            writer.writerow([col.get_text(strip=True) for col in header_columns])

        tbody = table.find('tbody')
        if not tbody:  
            tbody = table

        for row in tbody.find_all('tr'):
            columns = row.find_all('td')
            if columns:
                # Write row data to the CSV inside the 'with' block
                writer.writerow([col.get_text(strip=True) for col in columns])
    else:
        print("No table found in the response.")

print("Data has been scraped and saved to 'scraped_data.csv'")
