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
    # options.headless = True  # Enable headless mode for invisible operation
    # options.add_argument("--window-size=1920,1200")  # Define the window size of the browser

    # Set the path to the Chromedriver

    DRIVER_PATH = file_path.parent.parent / "data" / "laptop" / "msedgedriver.exe"
    # "/mnt/c/Users/tnguy/personal_projects/selenium_scraping/selenium_webscraping/data/Driver_Notes_edge/msedgedriver.exe"
    # DRIVER_PATH = r"C:\Users\tnguy\personal_projects\selenium_scraping\selenium_webscraping\data\Driver_Notes_edge\msedgedriver.exe"
    # logger.info(f"Current driver path: {DRIVER_PATH}")
    # return

    # Initialize Chrome with the specified options
    # edge_service = Service(executable_path=DRIVER_PATH, verbose=True)
    # # service = Service(verbose = True)
    driver = webdriver.Edge(options=edge_options)
    # service = Service()
    # options = webdriver.ChromeOptions()
    # driver = webdriver.Chrome(service=service, options=options)

    # Navigate to the Nintendo website
    # driver.get("https://www.kroger.com/")

    # # Output the page source to the console
    # # print(driver.page_source)
    # html = driver.page_source

    # # Close the browser session cleanly to free up system resources
    # driver.quit()

    # soup = BeautifulSoup(html, "html.parser")
    # titles = soup.find_all("span", class_="kds-Text--m text-primary font-secondary font-medium mt-0")
    # logger.info(f"Html: {html}")
    # logger.info(f"Soup: {soup}")
    # logger.info(f"Titles: {titles}")
    driver.get("https://www.brainyquote.com/")
    # driver.get("https://www.python.org")
    # search = driver.find_element_by_xpath("//div[@class='input-container']")
    # logger.info(search)
    # Retrieve the page source
    # html = driver.page_source
    time.sleep(3)

    # Find the search bar element
    search_bar = driver.find_element(By.NAME, 'q')

    # Enter a search term
    search_bar.send_keys('inspiration')

    # Submit the search
    search_bar.send_keys(Keys.RETURN)

    # Allow some time for the results to load
    time.sleep(3)

    # Find and print the search results
    results = driver.find_elements(By.CLASS_NAME, 'bqQt')
    for result in results:
        print(result.text)

    # Close the browser
    driver.quit()

    # # Close the driver
    # driver.quit()

    # # Parse the HTML with BeautifulSoup
    # soup = BeautifulSoup(html, 'html.parser')

    # # Find all 'tr' elements with class 'athing' which contain the news titles
    # titles = soup.find_all('tr', class_='athing')

    # # # Loop through each title and print it
    # # for title in titles:
    # #     # Find the <a> tag within the 'titleline' span inside a 'td' with class 'title'
    # #     title_link = title.find('td', class_='title').find('span', class_='titleline').find('a')
    # #     title_text = title_link.get_text()  # Extract the text of the title
    # #     print(title_text)
    # logger.info(f"Titles: {soup}")

if __name__ == "__main__":
    main()