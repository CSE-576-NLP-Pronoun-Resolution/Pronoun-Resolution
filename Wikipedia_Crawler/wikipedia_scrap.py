import wikipedia
import csv
import re
import collections
import spacy
#print(wikipedia.summary("Python"))
"""result = wikipedia.search("Nature")
print(result)
page = wikipedia.page(result[0])
title = page.title
content = page.content
print(type(content))
idx = content.find("== See also ==")
content = content[0:idx]
x = re.findall("==.*==.*", content)
for s in x:
	content = content.replace(s,"\n")
content = content.replace("\n","")
print(content)
print(page.url)
print(x)
wikifile = open("wikipedia_db.csv",mode='w')
wikiwriter = csv.writer(wikifile, delimiter=',')
wikiwriter.writerow([content,page.url])
print("==========================================================")
print("Page Summary",page.summary,"\n")
print("==========================================================")
print("Page Title: ",title,"\n")
print("==========================================================")
print("Page Contents: ",content,"\n")
print("==========================================================")
links = page.links
print("Page Links: ",links,"\n")

page = wikipedia.page(links[0])
title = page.title
content = page.content
print("==========================================================")
print("Page Summary",page.summary,"\n")
print("==========================================================")
print("Page Title: ",title,"\n")
print("==========================================================")
print("Page Contents: ",content,"\n")
print("==========================================================")
print("Page Links: ",page.links,"\n")"""
wikifile = open("wikipedia_db.csv",mode='w')
def pagescrape(page):
	title = page.title
	content = page.content
	url = page.url
	print("Scraping.....",title," : ",url)
	idx = content.find("== See also ==")
	content = content[0:idx]
	x = re.findall("==.*==.*", content)
	for s in x:
		content = content.replace(s,"")
	content = content.replace("\n","")
	print("Writing in CSV file....")
	wikiwriter = csv.writer(wikifile, delimiter=',')
	wikiwriter.writerow([title,content,url])

def main():
	result = wikipedia.search("Enola Holmes (film)")
	queue = collections.deque([]) 
	expanded = []
	nlp = spacy.load("en_core_web_sm")
	page = wikipedia.page(result[0])
	queue.append(page)
	#wpage = wikipedia.WikipediaPage(result[0])
	#print(wpage.categories)
	i = 0
	while len(queue) != 0:
		print("Getting the page from queue....")
		page = queue.popleft()
		if page in expanded:
			continue
		expanded.append(page)
		pagescrape(page)
		links = page.links
		print("Looking for links in page....")
		numberlinks = 0
		for l in links:
			try:
				if(numberlinks == 10):
					break
				p = wikipedia.search(l)
				disam = re.findall("(disambiguation)", p[0])
				if len(disam) != 0:
					continue
				doc = nlp(p[0])
				found_name = 0;
				for ent in doc.ents:
					if(ent.label_ == 'PERSON'):
						found_name = 1
						break
				if(found_name == 0):
					continue
				print("Link: ",p[0])
				numberlinks += 1
				if p[0] not in queue:
					queue.append(wikipedia.page(p[0]))
			except wikipedia.exceptions.PageError:
				continue
			except wikipedia.exceptions.DisambiguationError:
				continue
		i += 1
		if(i == 10):
			return
	
main()