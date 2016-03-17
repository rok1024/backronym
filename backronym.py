"""
    First, we must develop an API for thesaurus.com, as all the current ones are crap.

    When searching a word (ex: "small"), the synonyms are grouped into three
    categories, differing in presentation by a change in the background color
    of their <span> object.

    The categories are as follows:
        relevant-1
        relevant-2
        relevant-3

    The higher the integer suffix, clearly, the more relevant it is.

    ----------

    Now that I have the synonym "finding" down, I need to be able to expand the
    search on top-level synonyms if there are no findings for a given word.
"""
# external libraries
import requests
from bs4 import BeautifulSoup

def printAll(list):
    for item in list:
        print(item)

def findSynonyms2(inputWord,letter):
    print("Searching " + inputWord)
    syn3 = []
    syn2 = []
    syn1 = []
    goodWords = []
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant-3":
                syn3.append(word.text)
            elif relevanceLevel == "relevant-2":
                syn2.append(word.text)
            elif relevanceLevel == "relevant-1":
                syn1.append(word.text)
            else:
                break

        for word in syn3:
            if word[0] == letter:
                goodWords.append("3 - " + word)

        for word in syn2:
            if word[0] == letter:
                goodWords.append("2 - " + word)

        for word in syn1:
            if word[0] == letter:
                goodWords.append("1 - " + word)

def findSynonyms(inputWord,letter):
    syn3 = []
    syn2 = []
    syn1 = []
    goodWords = []
    # set up the soup of beauty
    url = "http://www.thesaurus.com/browse/" + inputWord
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # check to see if there are actually synonyms for the entry.
    errorTag = soup.select("#words-gallery-no-results")
    if errorTag != []:
        errorText = [item.text for item in errorTag][0]
        print(errorText)
    else:
        wordTags = soup.select("span.text")

        for word in wordTags:
            relevanceLevel = word.parent.attrs["data-category"].rsplit("name\": \"")[1].rsplit("\",")[0]
            if relevanceLevel == "relevant-3":
                syn3.append(word.text)
            elif relevanceLevel == "relevant-2":
                syn2.append(word.text)
            elif relevanceLevel == "relevant-1":
                syn1.append(word.text)
            else:
                break

        for word in syn3:
            if word[0] == letter:
                goodWords.append("3 - " + word)

        for word in syn2:
            if word[0] == letter:
                goodWords.append("2 - " + word)

        for word in syn1:
            if word[0] == letter:
                goodWords.append("1 - " + word)

        if goodWords == []:
            print("No words found. Searching top level synonyms for more...")
            """
                Here, we shall go through the syn3 words, looking at their
                synonyms, and printing them out if they start with the same letter.
            """
            for word in syn3:
                findSynonyms2(word,letter)

inputWord = raw_input("What word would you like to make?\n > ").lower()
words = raw_input("Type " + str(len(inputWord)) + " words that describe it.\n > ").lower().split(" ")
for x in xrange(0,len(inputWord)):
    newWord = words[x]
    lineString = "-" * len(newWord)
    print("\n" + newWord + ":\n" + lineString)
    if newWord[0] == inputWord[x]: # if they already start with the same letter
        print(newWord)
    else:
        findSynonyms(newWord,inputWord[x])
