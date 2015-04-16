# packages to import
import urllib2
from bs4 import BeautifulSoup
import re

# step 1
# getting the list of all the domestic urls to scrape
url_domestic_list = []
page_number = range(0,135)
for i in page_number:
    url_domestic_list.append("http://www.boxofficemojo.com/alltime/domestic.htm?page=" + str(page_number[i]) + "&p=.htm")

# step 2       
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
    for id in id_list:
        movie_url_to_scrape.append("http://www.boxofficemojo.com/movies/?id" + id)
    movie_url_to_scrape_unique = set(movie_url_to_scrape)
 
# step 3   
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

# step 4
# creating empty lists to store data...this step can be changed later
movie_title = []
movie_dtg = []
movie_runtime = []
movie_rating = []
movie_release_date = []


# looping through and scraping elements from each movie url!!
for movie in movie_url_to_scrape:
    page = urllib2.urlopen(movie)
    soup = BeautifulSoup(page)
    title_string = soup.find("title").text
    title =  title_string.split(" (")[0].strip()
    dtg = get_movie_value(soup, "Domestic Total")
    runtime = get_movie_value(soup, "Runtime")
    rating = get_movie_value(soup, "MPAA Rating")
    release_date = get_movie_value(soup, "Release Date")
    movie_title.append(title)
    movie_dtg.append(dtg)
    movie_runtime.append(runtime)
    movie_rating.append(rating)
    movie_release_date.append(release_date)

# looping through and scraping foreign revenue elements
foreign_dict = {}
for movie in movie_url_to_scrape:
    page = urllib2.urlopen(movie)
    soup = BeautifulSoup(page)
    rows = soup.find('table', border="3").find('tr').find_all(bgcolor="#ffffff")
	title = soup_foreign_5year.find('title').get_text().split(" (")[0]
	for row in rows:
    	cells = row.find_all("td")
    	foreign_dict.setdefault(title, []).append(tuple((cells[0].get_text(), cells[5].get_text()))

  

