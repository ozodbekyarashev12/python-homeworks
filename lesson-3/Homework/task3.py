import requests
from bs4 import BeautifulSoup
import json

BASE_URL = "https://www.demoblaze.com"
LAPTOPS_SECTION_URL = BASE_URL + "/prod.html#laptops"

def get_page_soup(url):
    """
    Given a URL, fetch the page and return a BeautifulSoup object.
    """
    response = requests.get(url)
    return BeautifulSoup(response.content, 'html.parser')

def get_laptops_from_page(soup):
    """
    Given a BeautifulSoup object, extract laptop data and return it in a structured format.
    """
    laptops = []

    # Find all the laptop containers on the page
    laptop_containers = soup.find_all('div', class_='card')
    
    for container in laptop_containers:
        # Extract the laptop name, price, and description
        name = container.find('h4', class_='card-title').text.strip()
        price = container.find('h5').text.strip()  # Price is within <h5> tags
        description = container.find('p').text.strip()  # Description is within <p> tags
        
        laptops.append({
            "name": name,
            "price": price,
            "description": description
        })
    
    return laptops

def get_next_page_url(soup):
    """
    Check if the "Next" page button exists and return the next page URL.
    """
    next_button = soup.find('a', {'class': 'page-link', 'aria-label': 'Next'})
    if next_button:
        return BASE_URL + next_button['href']
    return None  # Return None if no next page is found

def scrape_laptops():
    """
    Main function to scrape laptop data from all pages of the Laptops section.
    """
    all_laptops = []
    url = LAPTOPS_SECTION_URL
    
    while url:
        print(f"Scraping {url}...")
        soup = get_page_soup(url)
        
        # Extract laptops from the current page
        laptops = get_laptops_from_page(soup)
        all_laptops.extend(laptops)
        
        # Get next page URL
        url = get_next_page_url(soup)
    
    return all_laptops

def save_to_json(data, filename='laptops.json'):
    """
    Save the data to a JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Data saved to {filename}")

def main():
    # Scrape laptop data
    laptops = scrape_laptops()
    
    # Save the scraped data to JSON file
    save_to_json(laptops)

if __name__ == "__main__":
    main()
