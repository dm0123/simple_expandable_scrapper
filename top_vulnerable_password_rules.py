"""
    Rules for different sites
"""
from expandable_scrapper_base import *

class SecurityDotRuRule(ScrapperRule):
    def apply(self, document):
        table = document.find_class("tablez").pop()
        rows = table.findall('tr')
        mapped = map(lambda x: x.getchildren()[1].text, rows)
        return mapped

class VKBlogDotRuRule(ScrapperRule):
    """
            This rule retrieves only one password
            because page is broken (contains not
            closed break tags)
    """

    def apply(self, document):
        div_with_content = document.find_class("entry").pop()
        paragraphs = div_with_content.findall(".//p")
        return paragraphs[1].text.split("<br>")

class XakerDotRuRule(ScrapperRule):
    def apply(self, document):
        div_with_content = document.find_class("bdaia-post-content").pop()
        table = div_with_content.findall("table").pop()
        rows = table.findall(".//tr")
        mapped = map(lambda x: x.getchildren()[0].text, rows)
        return filter(lambda x: x is not None, mapped)


scrapper_rules = {
    "security.ru"   : {
                        "address"   : "http://www.securrity.ru/worstpwdz.html",
                        "rule"      : SecurityDotRuRule
    },
    "vkblog.ru"     : { 
                        "address"   : "http://vkblog.ru/bezopasnost/200-samykh-populyarnykh-parolejj-v-internete/",
                        "rule"      : VKBlogDotRuRule
    },
    "xaker.ru"      : {
                        "address"   : "https://xakep.ru/2015/09/15/ashley-madison-passwords-2/",
                        "rule"      : XakerDotRuRule
    }
}