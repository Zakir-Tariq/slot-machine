import requests
import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, features="html.parser")
    for link in soup.findAll('a'):
        content = str(link.string)
        words = content.lower().split()
        for word in words:
            word_list.append(word)
    clean_the_words(word_list)

def clean_the_words(words):
    clean_word_list = []
    symbols = "!@#$%^&*()_+-={}[]:\";'<>,.?/|"
    for word in words:
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            print(word)
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in clean_word_list:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key , value in sorted(word_count_items(),key=operator.itemgetter(1)):
        print(key, value)




start("https://www.scrapingbee.com/blog/crawling-python/")