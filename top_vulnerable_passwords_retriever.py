"""
    Script retrieves most vulnerable passwords
    from web page
"""

from lxml import html
from expandable_scrapper_base import *
import sys,traceback

class TopVulnerablePasswordsRule(ScrapperRule):

    def apply(self, document):
        # TODO: harcdoded class for now
        table = document.find_class("tablez").pop()
        rows = table.findall('tr')
        mapped = map(lambda x: x.getchildren()[1].text, rows)
        return mapped

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        raise Exception('Please, set url as first argument and filename as second')

    url = sys.argv[1]
    filename = "output.txt" if argc < 3 else sys.argv[2]

    try:
        print('*** Starting to work...')
        scrapper = ExpandableScrapperBase(url)
        rule = TopVulnerablePasswordsRule()
        scrapper.scrap(rule)
        print('*** Saving...')
        scrapper.save(filename)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)
    print('*** Done! Open %s to see output.'%filename)