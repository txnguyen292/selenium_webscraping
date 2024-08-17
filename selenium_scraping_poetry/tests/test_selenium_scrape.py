import sys
from pathlib import Path

file_path = Path(__file__).resolve().parent
scripts_path = file_path.parent / "selenium_scraping_poetry"
sys.path.append(str(scripts_path))

from scrape_for_test import main

def test_main():
	title = main()
	assert title == "Welcome to Python.org"