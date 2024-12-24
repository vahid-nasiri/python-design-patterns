from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests

# Requirements :
# 'beautifulsoup4' and 'requests'.


class WebScraperTemplate(ABC):
    @abstractmethod
    def send_request(self, url):
        """Abstract method for sending HTTP requests."""
        pass

    @abstractmethod
    def parse_html(self, content):
        """Abstract method for parsing HTML content."""
        pass

    @abstractmethod
    def extract_data(self, soup):
        """Abstract method for extracting data from parsed HTML."""
        pass

    def scrape_website(self, url):
        """The template method for web scraping."""
        content = self.send_request(url)
        soup = self.parse_html(content)
        data = self.extract_data(soup)
        return data


class BSWebScraper(WebScraperTemplate):
    def send_request(self, url):
        """Concrete implementation for sending HTTP requests using requests library."""
        response = requests.get(url)
        return response.content

    def parse_html(self, content):
        """Concrete implementation for parsing HTML content using BeautifulSoup."""
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def extract_data(self, soup: BeautifulSoup):
        """Concrete implementation for extracting data from parsed HTML."""
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links

# Example of usage


def main():
    bs_web_scraper = BSWebScraper()
    target_url = "https://google.com"

    print("Scraping Data by BeautifulSoup WebScraper: ")
    results = bs_web_scraper.scrape_website(target_url)
    for link in results:
        print(link)


if __name__ == "__main__":
    main()
