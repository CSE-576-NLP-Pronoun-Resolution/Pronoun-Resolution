import pprint 
import requests
import json
import csv
import re
from types import SimpleNamespace
from bs4 import BeautifulSoup
from time import sleep

def writeToCSV(query_term, icount):
    secret = "7sfsQiTVkLW6tv46UeQicplv8snUjbJZ"

    # Define the endpoint 

    url = 'https://api.nytimes.com/svc/movies/v2/reviews/search.json'
    # Specify the query and 
    # number of returns 
    sleep(0.06)
    # Make the request
    url = url + "?query="+query_term+"&api-key="+secret+"&num_results=50"
    response = requests.get(url)
    #print(str(url))
    response_json = response.json()
    #print(str(response_json))
    # fields = ('Title', 'Content', 'URL')
    wikifile = open("movie_reviews.csv",mode='a', newline='')
    # wikifile = csv.DictWriter("news_article.csv", fieldnames=fields, lineterminator = '\n')
    

    MyFile=open('ExpandedListMovies.txt','r')
    expanded = []
    lines = MyFile.read().splitlines()
    for x in lines:
        expanded.append(x+"\n")
    MyFile.close()
    tempicount = icount
    if('results' in response_json and response_json['results'] and len(response_json['results']) and response_json['results'][0]):
        for i in range(len(response_json['results'])):
            print("^^^^"+str(len(response_json['results']))+"^^"+query_term)
            if(response_json['results'][i] == None or 'link' not in response_json['results'][i] or response_json['results'][i]['link'] == None or 'url' not in response_json['results'][i]['link']):
                print("Format does not contain link and results")
                continue
            url = response_json['results'][i]['link']['url']
            #print("Writing in 1 ---------- "+str(i))
            if url+"\n" in expanded:
                print(str(url) + " query " + query_term)
                continue
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            title = soup.title.text # gets you the text of the <title>(...)</title>

            if(len(soup.select('article')) <= 0 or len(soup.select('article')[0].select('section')) <=0):
                print("No articles found (maybe!)")
                continue

            content = ""
            #print(str(soup.select('article')[0].select('section')))
            section_content = soup.select('article')[0].select('section')
            if(section_content and len(section_content)>0):
                for sect_itr in range(len(section_content)):
                    if("@media" in str(section_content[sect_itr]) or "<style>" in str(section_content[sect_itr]) or "Full text is unavailable for this digitized archive article" in str(section_content[sect_itr])):
                        continue
                    content = section_content[sect_itr].text
                    break
            if(content == ""):
                print("Content is still empty")
                continue

            if("@media" in content or "<style>" in content or "Full text is unavailable for this digitized archive article" in content):
                print("Could not find article")
                continue

            if(len(content) < 750):
                print("Too Short")
                continue


            div_tag = ""
            figure_tag = ""
            figure_caption_tag = ""
            img_tag = ""

            if("—" in str(content)):
                index = content.index("—")
                content = content[index+1:len(content)]
            if(len(soup.select('article')) >0 and len(soup.select('article')[0].select('section')) >0 and (soup.select('article')[0].select('section')[0].div!=None)):
                div_tag = soup.select('article')[0].select('section')[0].div.text
                # for i in range(len(soup.select('article')[0].select('section')[0].select('div')))
                    # content = content.replace(soup.select('article')[0].select('section')[0].select('div')[i].text, "")

            if(len(soup.select('article')) >0 and len(soup.select('article')[0].select('section')) >0 and soup.select('article')[0].select('section')[0].figure!=None):
                figure_tag = soup.select('article')[0].select('section')[0].figure.text
                for i in range(len(soup.select('article')[0].select('section')[0].select('figure'))):
                    content = content.replace(soup.select('article')[0].select('section')[0].select('figure')[i].text, "")

            if(len(soup.select('article')) >0 and len(soup.select('article')[0].select('section')) >0 and soup.select('article')[0].select('section')[0].figcaption!=None):
                figure_caption_tag = soup.select('article')[0].select('section')[0].figcaption.text
                for i in range(len(soup.select('article')[0].select('section')[0].select('figcaption'))):
                    content = content.replace(soup.select('article')[0].select('section')[0].select('figcaption')[i].text, "")

            if(len(soup.select('article')) >0 and len(soup.select('article')[0].select('section')) >0 and soup.select('article')[0].select('section')[0].img!=None):
                img_tag = soup.select('article')[0].select('section')[0].img.text
                for i in range(len(soup.select('article')[0].select('section')[0].select('img'))):
                    content = content.replace(soup.select('article')[0].select('section')[0].select('img')[i].text, "")

            content = content.replace("\n"," ")
            content = content.replace("Getty Images", "")
            #print("Writing in 4")
            x = re.findall("\s\s+", content)
            for s in x:
                content = content.replace(s," ")

            x = re.findall("\.[A-Z]", content)
            for h in x:
                content = content.replace(h,h[0]+" "+h[1])

            x = re.findall("\.“", content)
            for h in x:
                content = content.replace(h,h[0]+" "+h[1])

            x = re.findall("\.”[A-Z]", content)
            for h in x:
                content = content.replace(h,h[0]+h[1]+" "+h[2])

            # content = content.replace(div_tag, "")
            # content = content.replace(figure_tag, "")
            # content = content.replace(figure_caption_tag, "")
            # content = content.replace(img_tag, "")

            print("Writing in CSV******* " + str(tempicount))
            content = content.strip()
            
            wikiwriter = csv.writer(wikifile, delimiter=',')
            try:
                wikiwriter.writerow([title,content,url])
                tempicount = tempicount+1

            except UnicodeEncodeError:
                print("UnicodeEncodeError!")
                continue
            except JSONDecodeError:
                print("JSONDecodeError!")
                continue
            except AttributeError:
                print("AttributeError!")
                continue
            
            expanded.append(url+"\n")
            if(tempicount == 20000):
                    break

            

    wikifile.close()
    MyFile=open('ExpandedListMovies.txt','w')
    MyFile.writelines(expanded)
    MyFile.close()
    return tempicount

search_terms_file=open('movie_terms.txt','r')
query_list = search_terms_file.read().splitlines()
query_test = ["batman","avengers"]
icount = 0
for i in range(len(query_list)):
    icount = writeToCSV(query_list[i], icount)