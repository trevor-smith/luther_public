# packages to import
import urllib2
from bs4 import BeautifulSoup
import re
import pickle


# getting the list of all the domestic urls to scrape
# this will help get us the list of movies and their respective id's
# with these page id's we can construct the url list to scrape
url_domestic_list = []
page_number = range(0,135)
for i in page_number:
    url_domestic_list.append("http://www.boxofficemojo.com/alltime/domestic.htm?page=" + str(page_number[i]) + "&p=.htm")
       
# looping through all the domestic url pages and scraping the movie urls
id_list = []
movie_url_to_scrape = []
for url in url_domestic_list:
    page_domestic = urllib2.urlopen(url)
    soup_domestic = BeautifulSoup(page_domestic)
    # need to encode this as utf-8 or else it throws error
    # for the a attribute, look for hrefs that start with '/movies/?'
    href_movie_tags = [(a.attrs.get('href')).encode('utf-8') for a in soup_domestic.select('a[href^/movies/?]')]
    # splitting the hrefs based on movie id
    href_movie_tags_split = [i.split('id', 1) for i in href_movie_tags]
    # create a list of only the movie ids
    for i in href_movie_tags_split[:-1]:
        id_list.append(i[1])
    id_list_unique = set(id_list)
	# creating the list of movie urls that we will be scraping
	# this is done by using a templated url and adding the id to make a valid movie url
    for id in id_list:
        movie_url_to_scrape.append("http://www.boxofficemojo.com/movies/?id" + id)
    movie_url_to_scrape_unique = set(movie_url_to_scrape)
    
# saving the list to my local so I can access it later
# this uses pickle
with open('list_of_movie_urls.pkl', 'w') as f:
    pickle.dump(movie_url_to_scrape_unique, f)
    
# now to open it back up to use another time
with open('list_of_movie_urls.pkl', 'r') as f:
    domestic_urls = pickle.load(f)
# now the object 'domestic_urls' will have all the urls we previously scraped

# need to split the domestic urls because we need to add in '?page=intl&'
# this will take us to the foreign box office page where we scrape international country revenue
domestic_split_urls = []
for url in domestic_urls:
    domestic_split_urls.append(url.split("?"))
    
# getting foreign urls by just augmenting the domestic movie urls
foreign_urls = []
for url in domestic_split_urls:
    foreign_urls.append(url[0] + "?page=intl&" + url[1])

# saving the list to my local so I can access it later
with open('foreign_urls.pkl', 'w') as f:
    pickle.dump(foreign_urls, f)

# this is how I could load the foreign urls from my local
 with open('foreign_urls.pkl', 'r') as f:
    foreign_urls = pickle.load(f)

# function for scraping the webpage
def get_movie_value(soup, field_name):
    """
    takes a string attribute of a movie on the page, and
    returns the string in the next sibling object (the value for that attribute)
    """
    obj = soup.find(text = re.compile(field_name))
    if not obj:
        return None
    next_sibling = obj.findNextSibling()
    if next_sibling:
        return next_sibling.text
    else:
        return None


# import domestic urls from local
with open('list_of_movie_urls.pkl', 'r') as f:
    domestic_urls = pickle.load(f)

# looping through and scraping elements from each movie url!!
domestic_dict = {}

for movie in domestic_urls:
    movie = str(movie)
    hdr = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"}
    req = urllib2.Request(movie, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except:
        print movie
    else:
        soup = BeautifulSoup(page)
        title_string = soup.find("title").text
        title =  title_string.split(" (")[0].strip()
        dtg = get_movie_value(soup, "Domestic Total")
        runtime = get_movie_value(soup, "Runtime")
        rating = get_movie_value(soup, "MPAA Rating")
        release_date = get_movie_value(soup, "Release Date")
        genre = get_movie_value(soup, "Genre: ")
        production_budget = get_movie_value(soup, "Production Budget")
        worldwide = get_movie_value(soup, "Worldwide:")
        director = get_movie_value(soup, "Director")
        writers = get_movie_value(soup, "Writers:")
        actors = get_movie_value(soup, "Actors:")
        domestic_dict.setdefault(title, []).append(tuple((dtg, runtime, rating, release_date, genre,
                                                             production_budget)))
    	

# import foreign_urls from local
with open('foreign_urls.pkl', 'w') as f:
    foreign_urls = pickle.load(f)

# looping through and scraping foreign revenue elements
foreign_dict = {}
for movie in foreign_urls:
    hdr = {'User-Agent' : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36"}
    req = urllib2.Request(movie, headers=hdr)
    try:
        page = urllib2.urlopen(req)
    except:
        print movie
    else:
        soup = BeautifulSoup(page)
        rows_odd = soup.find('table', border="3").find('tr').find_all(bgcolor="#ffffff")
        rows_even = soup.find('table', border="3").find('tr').find_all(bgcolor="#f4f4ff")
        title = soup.find('title').get_text().split(" (")[0]
        for row in rows_odd:
            cells = row.find_all("td")
            #print tuple((cells[0].get_text(), cells[5].get_text()))
            try:
                foreign_dict.setdefault(title, []).append(tuple((cells[0].get_text(), cells[5].get_text())))
            except:
                None
            else:
                None
        for row in rows_even:
            cells = row.find_all("td")
            try:
                foreign_dict.setdefault(title, []).append(tuple((cells[0].get_text(), cells[5].get_text())))
            except:
                None
            else:
                None
            #print tuple((cells[0].get_text(), cells[5].get_text()))
  

