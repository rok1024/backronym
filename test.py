import requests
from bs4 import BeautifulSoup

url = "http://www.thesaurus.com/browse/a"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")


# Just in case...

    # if syn3 != []:
    #     print("Level 3 Synonyms")
    #     printAll(syn3)
    #
    # if syn2 != []:
    #     print("Level 2 Synonyms")
    #     printAll(syn2)
    #
    # if syn1 != []:
    #     print("Level 1 Synonyms")
    #     printAll(syn1)
