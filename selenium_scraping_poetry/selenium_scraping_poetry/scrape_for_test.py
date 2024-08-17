import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from loguru import logger
from bs4 import BeautifulSoup
from pathlib import Path
from selenium.webdriver.common.keys import Keys
file_path = Path(__file__).resolve().parent

def main():
    # Set up options for headless Chrome
    edge_options = Options()
    edge_options.add_argument('--headless')  # Run in headless mode
    edge_options.add_argument('--disable-gpu')  # Disable GPU usage (optional)
    edge_options.add_argument('--window-size=1920,1200')

    driver = webdriver.Edge(options=edge_options)
    driver.get("https://www.python.org")


    # Allow some time for the results to load
    time.sleep(3)
    title = driver.title

    # Close the browser
    driver.quit()
    return title

if __name__ == "__main__":
    title = main()
    print(title)