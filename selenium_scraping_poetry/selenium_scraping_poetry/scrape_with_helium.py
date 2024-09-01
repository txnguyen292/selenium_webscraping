import helium
from loguru import logger
from typing import List, Tuple, Union, Optional, Dict
import json

def save_data_to_json(data: List[Dict[str, str]], save_path: str) -> None:
	with open(save_path, 'w') as fout:
		json.dump(data, fout)
	return


def get_author_quotes(page_link: str, keyword: str) -> Tuple[List[helium.S], List[helium.S]]:
	# helium.start_chrome("http://www.quotationspage.com/")
	helium.start_chrome(page_link)
	homesearch = helium.S("@homesearch")
	helium.write(keyword, into=homesearch)
	helium.click("Search")
	quotes = helium.find_all(helium.S("dl > dt"))
	authors = helium.find_all(helium.S("dl > dd"))
	helium.kill_browser()
	return quotes, authors

def combine_quotes_authors_into_data_structure(quotes: List[helium.S], authors: List[helium.S]) -> List[Dict[str, str]]:
	author_quote_list: List[Dict[str, str]] = []
	for (quote, author) in zip(quotes, authors):
		author_quote_dict: Dict[str, str] = {"Author": author.web_element.text, "Quote": quote.web_element.text}
		author_quote_list.append(author_quote_dict)
	return author_quote_list

def main():
	page_link = "http://www.quotationspage.com/"
	keyword = "einstein"
	save_path = r"C:\Users\tnguy\personal_projects\selenium_scraping\selenium_webscraping\data\scrape_data\authors_quotes.json"
	logger.info(f"Scraping author and quotes from {page_link} with keyword: {keyword}")
	quotes, authors = get_author_quotes(page_link=page_link, keyword=keyword)
	logger.info(f"Done getting quotes and authors")
	logger.info(f"Saving quotes and authors to path: {save_path}")
	author_quote_list = combine_quotes_authors_into_data_structure(quotes=quotes, authors=authors)
	save_data_to_json(data=author_quote_list, save_path=save_path)
	logger.info(f"Done saving data")
	return
if __name__ == "__main__":
	logger.info("Start scraping...")
	main()
	logger.info("Done scraping!!!")