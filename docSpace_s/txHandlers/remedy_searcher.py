from bs4 import BeautifulSoup
import requests
from txHandlers.remedy_database_access import RemedyDataBaseAccess
import pandas as pd
import time
from selenium import webdriver

'''
This class will perform the web scraping of below sites:
https://www.materiamedica.info/
http://www.homeoint.org/


Aim is to scrape different materia medica books and get 
remedies which matches the input symptoms

Example of request
        try:
            source = requests.get('https://www.imdb.com/chart/top', verify=False)
            source.raise_for_status()
            soup = BeautifulSoup(source.text, 'html.parser')
            movies = soup.find('tbody', class_='lister-list').find_all('tr')

            for movie in movies:
                name = movie.find('td', class_='titleColumn').a.text
                print(name)
                break

        except Exception as e:
            print(e)
'''

SOURCE_SITE_1 = "https://www.materiamedica.info"


class RemedySearcher:

    def __init__(self, remedy_db_controller):

        self.remedy_database_access = RemedyDataBaseAccess(remedy_db_controller)
        # self.update_source_1_to_db()

    def update_book_to_db(self, book_soup):
        # For each book we will get all the remedies present.
        # Get the remedy list first.
        remedy_url_tag_list = book_soup.find('div', class_="remedy_list").find_all('a')

        for remedy_url_tag in remedy_url_tag_list:
            # Remedy is nothing but the medicine name, formulate the URL
            # which will have all the information about the remedy.
            remedy_url = remedy_url_tag.attrs

            if 'href' in remedy_url:
                remedy_url = SOURCE_SITE_1 + remedy_url['href']

                # remedy_url is the URL of the actual medicine information.
                # We would send request to this url which will give the medicine
                # name and the paragraphs about the medicine which is nothing but
                # the symptom information for given medicine.
                remedy_soup = BeautifulSoup(requests.get(remedy_url, verify=False).text,
                                            'html.parser')

                # now the page has a div tag with attribute class with value content
                # within this we need to get the heading 1(h1) which gives the name of the
                # medicine.
                # The text after h1 gives the brief about the medicine get it using siblings
                header_tag_list = remedy_soup.find('div', class_='content').find_all('h1')

                print(remedy_url, "header tag list ", len(header_tag_list))

                # Currently there should be only one header, give a warning print
                # in case more then that.
                if len(header_tag_list) > 1:
                    print("Warning: got a header with more then one length ", len(header_tag_list))
                for i, header_tag in enumerate(header_tag_list):
                    print("header is ",  header_tag.text)
                    # This will get any text after the <h1> tag.
                    sibling = header_tag.next_sibling
                    print(sibling)

                remedy_soup = BeautifulSoup(requests.get(remedy_url, verify=False).text,
                                            'lxml')
                time.sleep(1)
                para = remedy_soup.find('body').find('div', class_='content').findAll('p')

                print("4444444444444444444444 ravneet looping ...", len(para), " - ", para)
                i = 0
                for para_t in para:
                    i = i + 1
                    print (i, "xxxxxxxxxxxxxxxxxxxxxxpara ravneet ")
                    print(para_t)
                    print(i, "xxxxxxxxxxxxxxxxxxxxxxpara ravneet done")

                    #if 'id' not in para_t.attrs:
                    #    print("----------------id attr", para_t.attrs)


    def update_source_1_to_db(self):

        try:
            source_1 = requests.get(SOURCE_SITE_1, verify=False)
            source_1.raise_for_status()

            soup = BeautifulSoup(source_1.text, 'html.parser')

            # this will get the list of tags for all matria medica books.
            book_tag_list = soup.find('ul', class_="content-author-blocks"). \
                find_all('li', class_="content-author-block")

            # iterate through each of the matria medica book tags.
            for index, book_tag in enumerate(book_tag_list):
                # we would now formulate given book URL and go to that.
                book_url = SOURCE_SITE_1 + book_tag.find('a').attrs['href']
                print("formulating data base for ", book_url)
                book_soup = BeautifulSoup(requests.get(book_url, verify=False).text,
                                      'html.parser')
                self.update_book_to_db(book_soup)
                # medica_tag.raise_for_status()

                break;

        except Exception as e:
            print(e)
