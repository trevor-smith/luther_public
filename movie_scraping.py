# packages to import
import urllib2
from bs4 import BeautifulSoup

# attributes for movie web page
url = "http://www.boxofficemojo.com/movies/?id=" + movie_name
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

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

# scraping the list of movie names
url_domestic = "http://www.boxofficemojo.com/alltime/domestic.htm?page=1&p=.htm"
page_domestic = urllib2.urlopen(url_domestic)
soup_domestic = BeautifulSoup(page_domestic)

# extracting only a tags with an href containing movies
href_movie_tags = [str(a.attrs.get('href')) for a in soup_domestic.select('a[href^/movies/?]')]
href_movie_tags_split = [i.split('id', 1) for i in href_movie_tags]

# extracting only id elements from the list above
# this will be used to construct the urls we loop through
id_list = []
for i in href_movie_tags_split[:-1]:
    id_list.append(i[1])
    
# constructing the url to loop through and scrape
movie_url_to_scrape = []
for id in id_list:
    movie_url_to_scrape.append("http://www.boxofficemojo.com/movies/?id" + id)
    
# constructing the domestic url to loop through and scrape list of movie names
page_number = range(1,13000)
url_domestic_static = "http://www.boxofficemojo.com/alltime/domestic.htm?page=" + num[i] + "&p=.htm"
for i in url_domestic_static:
    print i
    
url = "http://www.boxofficemojo.com/movies/?id=biglebowski.htm"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

# loop through all movie urls and scrape data!!
movie_title = []
movie_dtg = []
movie_runtime = []
movie_rating = []
movie_release_date = []
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

# getting the list of all the domestic urls to scrape
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
    for id in id_list:
        movie_url_to_scrape.append("http://www.boxofficemojo.com/movies/?id" + id)
    movie_url_to_scrape_unique = set(movie_url_to_scrape)   

