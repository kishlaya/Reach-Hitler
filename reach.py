import urllib.request
from bs4 import BeautifulSoup
import grequests

# ==========================================
# INTERNAL
# ==========================================

base = "https://en.wikipedia.org"

def get_random_wiki():
	# HOW DO I DO THIS NICELY?
	# EITHER USE HTML PARSER - OVERKILL?
	# OR MAYBE USE REGEX?

	url = base + "/wiki/Special:Random"
	res = urllib.request.urlopen(url).read().decode()
	s = res.find("<link rel=\"canonical\"")
	res = res[s:]
	e = res.find("\"/>")
	return res[52:e]

def generate_soup(html_doc):
	return BeautifulSoup(html_doc, "html.parser")

def get_wiki_content(soup):
	return soup.find(id="mw-content-text")

def get_wiki_links(content):
	links = []
	for link in content.find_all('a'):
		if not link.has_attr('href'):
			continue
		href = link.get('href')
		if href.startswith("/wiki/"):
			links.append(href)
	return links



# ==========================================
# MAIN FUNCTIONS
# ==========================================

def find_children(wiki):
	return get_wiki_links(get_wiki_content(generate_soup(wiki)))

def find_hitler_at(start_page, depth):
	hitler = "/wiki/Adolf_Hitler"

	# TODO: Make a graph so that parents can be tracked

	counter = 0
	page_list = [start_page]
	if hitler in page_list:
		return counter

	while counter<depth:
		counter = counter + 1

		requests = (grequests.get(base + wiki) for wiki in page_list)
		response = grequests.imap(requests)
		tmp = map(lambda x: find_children(x.content.decode()), response)
		page_list = sum(tmp, [])

		if hitler in page_list:
			return counter

	return -1

def find_hitler(start_page):
	return find_hitler_at(start_page, 5)


# ==========================================
# FIND HITLER
# ==========================================

start = get_random_wiki()
print("Starting at:", start)
level = find_hitler(start)
if level >= 0:
	print("Found at level ", level)
else:
	print("Not found")
