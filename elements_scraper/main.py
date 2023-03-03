import requests
from lxml import etree
from elements_scraper.scraper.scraper import find_red_underlined_elements_with_exclamation_mark,\
    find_red_underlined_elements


URL = 'https://developer.mozilla.org/de/docs/Web/API/Document'

response = requests.get(URL)
html = etree.HTML(response.content)


def main():

    print("\n[1] SHOW RED ELEMENTS")
    print("[2] SHOW RED ELEMENTS WITH EXCLAMATION(!) MARK")
    print("[any] EXIT\n")

    while True:

        menu_number = input("ENTER MENU NUMBER: ")
        if menu_number == '1':
            print('\n')
            [print(element) for element in find_red_underlined_elements(html)]
            print('\n')
        elif menu_number == '2':
            print('\n')
            [print(element) for element in find_red_underlined_elements_with_exclamation_mark(html)]
            print('\n')
        else:
            return


if __name__ == '__main__':
    main()
