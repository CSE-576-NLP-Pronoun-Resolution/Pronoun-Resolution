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
wikifile = open("wikipedia_db.csv",mode='a')
def pagescrape(page):
	title = page.title
	content = page.content
	
	if(len(content) < 1000):
		return;
	url = page.url
	print("Scraping.....",title," : ",url)

	idx = content.find("== See also ==")
	content = content[0:idx]

	x = re.findall("==.*==.*", content)
	for s in x:
		content = content.replace(s,"")
	content = content.replace("\n"," ")
	#re.sub('\n+'," ",content)
	
	x = re.findall("\s\s+", content)
	for s in x:
		content = content.replace(s," ")

	x = re.findall("\.[A-Z]", content)
	for h in x:
		content = content.replace(h,h[0]+" "+h[1])

	print("Writing in CSV file....")

	wikiwriter = csv.writer(wikifile, delimiter=',')
	wikiwriter.writerow([title,content,url])

def main():
	result = wikipedia.search("List of 20th-century writers")
	queue = collections.deque([]) 

	MyFile=open('ExpandedList.txt','r')
	expanded = []
	lines = MyFile.read().splitlines()
	for x in lines:
		expanded.append(x+"\n")
	MyFile.close()

	nlp = spacy.load("en_core_web_sm")
	page = wikipedia.page(result[0])
	queue.append(page)

	i = 0
	while len(queue) != 0:
		print("Getting the page from queue....")
		page = queue.popleft()

		if page.title+"\n" in expanded and page.title != "List of 20th-century writers":
			continue
		if page.title != "List of 20th-century writers":
			expanded.append(page.title+"\n")

		pagescrape(page)
		links = page.links
		
		print("Looking for links in page....")
		numberlinks = 0

		for l in links:
			try:
				if(numberlinks == 10):
					break
				p = wikipedia.search(l)
				if len(p) == 0 or p[0]+"\n" in expanded:
					continue
				doc = nlp(p[0])
				found_name = 0;

				for ent in doc.ents:
					if(ent.label_ == 'PERSON'):
						found_name = 1
						break;

				if(found_name == 0):
					continue
	
				if p[0] not in queue:
					queue.append(wikipedia.page(p[0]))
					numberlinks += 1
					print("Link: ",p[0])

			except wikipedia.exceptions.PageError:
				continue

			except wikipedia.exceptions.DisambiguationError:
				continue
		i += 1
		print("===================================")
		print("Number of Articles: ",i)
		print("===================================")
		if(i == 4):
			break

	MyFile=open('ExpandedList.txt','w')
	MyFile.writelines(expanded)
	MyFile.close()
	
main()
