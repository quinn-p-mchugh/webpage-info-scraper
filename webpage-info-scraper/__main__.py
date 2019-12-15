"""Module containing code to begin webpage scraping.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

def remove_words_from_text(text, words_to_remove):
    text_split = text.split()
    result_words = [word for word in text_split if word not in words_to_remove]
    result = ' '.join(result_words)
    return result

import csv
from pathlib import Path
from selenium import webdriver
from webpage import Webpage

with open(Path("webpage-info-scraper/webpage_urls.txt"), "r") as webpage_urls:
    with open(Path("webpage-info-scraper/webpage_data.csv"), "w") as webpage_data:
        writer = csv.writer(webpage_data, delimiter=",")
        web_driver = webdriver.Firefox()
        webpages = []
        """Scrape information from webpages using URLs stored in CSV file"""
        for url in webpage_urls:
            webpage = Webpage(url, web_driver)
            webpages.append(webpage)
            webpage.open()
            webpage.org_name = webpage.find_element_by_xpath("//h1").text
            print(webpage.org_name)

            try:
                contact_email_element = webpage.find_element_by_xpath("//span[text()='Contact Email']")
                div_text = contact_email_element.find_element_by_xpath('..').text
                webpage.email_address = remove_words_from_text(div_text, ['Contact', 'Email', 'E:'])
                print(webpage.email_address)
            except:
                webpage.email_address = ""

            writer.writerow([webpage.org_name, webpage.email_address])
