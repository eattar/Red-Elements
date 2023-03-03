from typing import List


def find_red_underlined_elements(html) -> List[str]:
    """takes an html and returns the founded red underlined elements from it"""
    # one red underlined element is not in the </code> block and does not follow the pattern. Therefore, it was scraped
    # separately.
    return html.xpath("//a[@class='page-not-created']/code/text() | //a[@class='page-not-created']/text()")


def find_red_underlined_elements_with_exclamation_mark(html) -> List[str]:
    """takes an html and returns the founded red underlined elements with exclamation mark from it"""
    # one red underlined element is not in the </code> block and does not follow the pattern. Therefore, it was scraped
    # separately.
    return html.xpath("//a[@class='page-not-created']"
                      "[following-sibling::abbr[@class='icon icon-nonstandard']]/code/text() | "
                      "//a[@class='page-not-created'][following-sibling::abbr[@class='icon icon-nonstandard']]/text()")
