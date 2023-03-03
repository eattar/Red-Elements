import unittest
from elements_scraper.scraper.scraper import find_red_underlined_elements, \
    find_red_underlined_elements_with_exclamation_mark
from elements_scraper.main import URL
from lxml import etree
import requests


class TestMain(unittest.TestCase):
    """this is a class for testing the scraper module"""

    def setUp(self) -> None:
        response = requests.get(URL)
        self.html = etree.HTML(response.content)

    def test_find_red_underlined_elements(self):
        """founded elements must be exactly 26"""
        self.assertEqual(len(find_red_underlined_elements(self.html)), 26)

    def test_find_red_underlined_elements_with_exclamation_mark(self):
        """founded elements must be exactly 3"""
        self.assertEqual(len(find_red_underlined_elements_with_exclamation_mark(self.html)), 3)

