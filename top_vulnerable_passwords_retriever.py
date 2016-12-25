"""
    Script retrieves most vulnerable passwords
    from web page
"""

from expandable_scrapper_base import ExpandableScrapperBase
from top_vulnerable_password_rules import scrapper_rules
import sys,traceback

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc < 2:
        raise Exception('Please, set url as first argument and filename as second')

    url = sys.argv[1]
    filename = "output.txt" if argc < 3 else sys.argv[2]

    try:
        print('*** Starting to work...')
        scrapper = ExpandableScrapperBase(scrapper_rules[url]["address"])
        rule = scrapper_rules[url]["rule"]()
        scrapper.scrap(rule)
        print('*** Saving...')
        scrapper.save(filename)
        print('*** Done! Open %s to see output.'%filename)
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                              limit=2, file=sys.stdout)