"""
 Simple expandable web scrapper. Uses lxml for html parse.
"""

from lxml import html

class ExpandableScrapperBase(object):
    """
        This class is base class for 
        certain web sites implementation
    """

    def __init__(self, url):
        self._url = url
        self._tree = html.parse(url)
        self._result = []

    def save(self, filename):
        """
            Save to file. It may be simple txt
            or complex .xls.
            Default implementation is write
            each row from result as new line.
        """
        with open(filename, mode="w", encoding="utf-8") as file:
            for row in self._result:
                file.write(row)
                file.write("\n")

    def scrap(self, rule):
        """
            Main method. Rule is instance of ScrapperRule
        """ 
        root = self._tree.getroot()
        self._result = rule.apply(root)

class ScrapperRule(object):
    """
        Rule object which modifies given document
    """

    def apply(self, document):
        """
            Returns modified document
        """
        return document