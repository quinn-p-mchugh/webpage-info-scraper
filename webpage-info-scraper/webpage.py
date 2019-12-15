"""Module defining classes and functions related to dating webpages.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException

class Webpage:
    """Represents a typical webpage.

    Attributes:
        url: A string containing the url of the webpage.
        web_driver: The web driver used open and utilize the webpage.
    """

    def __init__(self, url, web_driver):
        """Initializes Webpage class with url and web driver.
        """
        self.url = url
        self.web_driver = web_driver

    def open(self):
        """Opens the webpage using its specified url."""
        self.web_driver.get(self.url)

    def find_element_by_xpath(self, xpath):
        """Finds a web element by its xpath.

        Searches for the element until a certain time
        limit is reached, after which an exception is raised.

        Args:
            xpath: The xpath of the desired element.

        Returns:
            The element whose xpath matches the user-specified xpath.

        Raises:
            TimeoutException: The element was not found on the webpage
                before the time limit was reached.
        """
        try:
            element = WebDriverWait(self.web_driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, xpath)))
            return element
        except TimeoutException:
            print("Error: Timeout reached. Could not locate element with xpath: " + xpath)

    def click_button(self, xpath):
        """Clicks on an element with the specified xpath.

        Args:
            xpath: The xpath of the desired element.
        """
        self.find_element_by_xpath(xpath).click()

    def send_keys(self, xpath, input):
        """Sends keyboard input to an element with the a specified xpath.

        Args:
            xpath: The xpath of the desired element.
            input: The keyboard input to send."""
        self.find_element_by_xpath(xpath).send_keys(input)

    def switch_to_new_window(self):
        """Switches focus to a newly opened browser window."""
        num_windows_before = len(self.web_driver.window_handles)
        WebDriverWait(self.web_driver, 30).until(expected_conditions.number_of_windows_to_be(2))
        self.web_driver.switch_to_window(self.web_driver.window_handles[1])

    def switch_to_window_by_index(self, index):
        """Switches focus to a window by its index.

        Args:
            index: The index of the desired window.
        """
        self.web_driver.switch_to_window(self.web_driver.window_handles[index])
