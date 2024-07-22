from bs4 import BeautifulSoup
from bs4 import element
import requests
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import traceback

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
MAX_WORDS_TO_CONSIDER_NEW_ENTRY = 10
PRINT_DEBUG = True
CREATE_TABLE = "create table "
MAX_TEXT = " text(65535) "
class RemedySearcher:

    def __init__(self, db_controller):

        self.db_controller = db_controller
        # self.remedy_database_access = RemedyDataBaseAccess(remedy_db_controller)
        # self.update_source_1_to_db()


    # Adds the remedy to the list, it takes input as a tag
    # then adds a new entry in the list if that tag is good enough to be added.
    # returns true if remedy list is successfully appened or added false otherwise.
    @staticmethod
    def _add_to_remedy_list(remedy_list, remedy, remedy_tag):
        # Validate the tag first that it text only tag
        if remedy_tag is not None:
            # Input tag shouldn't have any child tag
            if len(remedy_tag.find_all()) != 0:
                return False
            # Input tag should not have any attributes
            if len(remedy_tag.attrs) != 0:
                return False

        # if remedy length is not zero and it doesn't contain whitespaces (' ', '\n' etc)
        if remedy is not None and len(remedy) != 0 and not remedy.isspace():
            # If remedy text is less then 5 we add it to the previous entry
            if len(remedy.split()) < MAX_WORDS_TO_CONSIDER_NEW_ENTRY:
                last_entry_idx = len(remedy_list) - 1
                remedy_list[last_entry_idx] = remedy_list[last_entry_idx] + " " + remedy
                # Return false here as we have updated existing remedy entry
                return False
            else:
                remedy_list.append(remedy)
                return True

        return False

    def update_book_to_db(self, book_soup, book_name):
        # For each book we will get all the remedies present.
        # Get the remedy list first.
        remedy_url_tag_list = book_soup.find('div', class_="remedy_list").find_all('a')

        all_remedy_list = []
        col_name_list = []
        is_col_name_set = False

        # Since all the paragraph which are present in the remedy URL are dynamically created/added
        # using request call with beautiful soup does not work.
        # Make a serenium chrome call which would load the URL and dynamically get the contents
        # for scraping.
        op = webdriver.ChromeOptions()
        op.ignore_zoom_level = True
        op.add_argument("--disable-extensions");
        op.add_argument("--disable-dev-shm-usage");
        op.add_argument("--no-sandbox");
        op.add_argument("--headless")
        op.add_argument("--disable-gpu")
        op.add_argument("--disable-infobars")
        op.add_experimental_option('excludeSwitches', ['enable-logging'])

        # chrome_service = ChromeService(ChromeDriverManager().install())
        # chrome_service.creationflags = CREATE_NO_WINDOW
        driver = webdriver.Chrome(options=op, service_args=['CREATE_NO_WINDOW'])

        for remedy_url_tag in remedy_url_tag_list:
            # Remedy is nothing but the medicine name, formulate the URL
            # which will have all the information about the remedy.
            remedy_url = remedy_url_tag.attrs
            remedy_info_text_list = []

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

                descriptions_added = 0
                # Currently there should be only one header, give a warning print
                # in case more then that.
                if len(header_tag_list) > 1:
                    print("Warning: got a header with more then one length ", len(header_tag_list))
                for i, header_tag in enumerate(header_tag_list):
                    print("header is ", header_tag.text)
                    remedy_info_text_list.append(header_tag.text)

                    if not is_col_name_set:
                        col_name_list.append("remedyName")

                    # This will get any text after the <h1> tag.
                    # Now we sometime have not needed tags after the header so we would iterate over all the
                    # siblings.
                    # please note since this gives static contents we would not be able to get the
                    # actual remedy paragraphs using siblings.

                    for sibling in header_tag.next_siblings:
                        # print ("sibling is of type ", type(sibling), " is ", isinstance(sibling, element.NavigableString))
                        i = i + 1
                        if isinstance(sibling, element.NavigableString):
                            ret = self._add_to_remedy_list(remedy_info_text_list, sibling, None)
                        else:
                            ret = self._add_to_remedy_list(remedy_info_text_list, sibling.text, sibling)

                        if ret:
                            descriptions_added += 1
                            if not is_col_name_set or descriptions_added >= len(col_name_list):
                                col_name_list.append("Description_" + str(descriptions_added))

                '''
                # Since all the paragraph which are present in the remedy URL are dynamically created/added
                # using request call with beautiful soup does not work.
                # Make a serenium chrome call which would load the URL and dynamically get the contents
                # for scraping.
                op = webdriver.ChromeOptions()
                op.ignore_zoom_lev      el = True
                op.add_argument("--disable-extensions");
                op.add_argument("--disable-dev-shm-usage");
                op.add_argument("--no-sandbox");
                op.add_argument("--headless")
                op.add_argument("--disable-gpu")
                op.add_argument("--disable-infobars")
                op.add_experimental_option('excludeSwitches', ['enable-logging'])

                # chrome_service = ChromeService(ChromeDriverManager().install())
                # chrome_service.creationflags = CREATE_NO_WINDOW
                driver = webdriver.Chrome(options=op, service_args=['CREATE_NO_WINDOW'])
                '''

                # driver = webdriver.Chrome()
                driver.get(remedy_url)
                time.sleep(3)

                remedy_soup = BeautifulSoup(driver.page_source, 'html.parser')
                # driver.close()

                # All the remedy details are added in different paragraph, we will add a new entry
                # in the remedy list for each paragraph.
                para_tag_list = remedy_soup.find('body').find('div', class_='content')

                if para_tag_list is None:
                    print(remedy_info_text_list)
                    para_tag_list = []
                else:
                    para_tag_list = para_tag_list.find_all('p')

                # print("4444444444444444444444 ravneet looping ...", len(para), " - ")
                # print( para)

                for remedy_para_tag in para_tag_list:
                    ret = self._add_to_remedy_list(remedy_info_text_list, remedy_para_tag.text, remedy_para_tag)
                    if ret:
                        descriptions_added += 1
                        if not is_col_name_set or descriptions_added >= len(col_name_list):
                            col_name_list.append("Description_" + str(descriptions_added))

                    # print (i, "xxxxxxxxxxxxxxxxxxxxxxpara ravneet ")
                    # print(para_t)
                    # print(i, "xxxxxxxxxxxxxxxxxxxxxxpara ravneet done")

                    # if 'id' not in para_t.attrs:
                    #    print("----------------id attr", para_t.attrs)

                is_col_name_set = True

            if len(remedy_info_text_list) != 0:
                all_remedy_list.append(remedy_info_text_list)

        # create a data frame from the complete remedy list.
        remedy_df = pd.DataFrame(all_remedy_list, columns=col_name_list)
        driver.close()

        '''
        create table now it in data base
        below is the how the data base create table example looks like:
        create table test( remedy_name varchar(50) not null,
					description1 text(65535),
					description2 text(65535));
		we will create a string after '(' using the column list we have
		this will be used to create different columns of the table in DB.
        '''
        table_str = book_name + " ("
        index = 0
        for col in col_name_list:
            table_str += (col + MAX_TEXT)
            if index + 1 == len(col_name_list):
                table_str += ");"
            else:
                table_str += " , "
            index += 1

        print (book_name)
        self.db_controller._db_create_table(table_str)
        self.db_controller.update_df_to_db(remedy_df, book_name)


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
                book_name = str(book_tag.find('a').attrs['href']).replace("/", "_")
                book_name = book_name.replace("-", "_")
                print("formulating data base for ", book_name)
                book_soup = BeautifulSoup(requests.get(book_url, verify=False).text,
                                          'html.parser')
                self.update_book_to_db(book_soup, book_name)
                # medica_tag.raise_for_status()


        except Exception as e:
            print(e)
            print(traceback.format_exc())
