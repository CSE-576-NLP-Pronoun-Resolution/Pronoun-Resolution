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
    url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
    # Specify the query and 
    # number of returns 
    parameters = { 
        'q': query_term, # query phrase 
        'page': 100, # maximum is 100 
        'api-key': secret # your own API key 
    } 
    sleep(6)
    # Make the request
    response = requests.get(url,params = parameters)

    response_json = response.json()
    #print(str(response_json))
    # fields = ('Title', 'Content', 'URL')
    wikifile = open("news_article.csv",mode='a', newline='')
    # wikifile = csv.DictWriter("news_article.csv", fieldnames=fields, lineterminator = '\n')
    

    MyFile=open('ExpandedListNews.txt','r')
    expanded = []
    lines = MyFile.read().splitlines()
    for x in lines:
        expanded.append(x+"\n")
    MyFile.close()
    tempicount = icount
    if('response' in response_json and response_json['response'] and 'docs' in response_json['response'] and response_json['response']['docs']):
        for i in range(len(response_json['response']['docs'])):
            #print("^^^^"+str(len(response_json['response']['docs']))+"^^"+query_term)
            url = response_json['response']['docs'][i]['web_url']
            #print("Writing in 1 ---------- "+str(i))
            if url+"\n" in expanded:
                continue
            #print("Writing in 2")
            response = requests.get(url)

            soup = BeautifulSoup(response.content, 'html.parser')

            title = soup.title.text # gets you the text of the <title>(...)</title>
            if(len(soup.select('article')) <= 0 or len(soup.select('article')[0].select('section')) <=0):
                continue

            content = soup.select('article')[0].select('section')[0].text
            #print("Writing in 3")

            if("@media" in content or "<style>" in content or "Full text is unavailable for this digitized archive article" in content or "See the article in its original context" in content):
                continue

            if(len(content) < 750):
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
            tempicount = tempicount+1
            if(tempicount == 0):
                break
            try:
                wikiwriter.writerow([title,content,url])
            except UnicodeEncodeError:
                continue
            except JSONDecodeError:
                continue
            except AttributeError:
                continue

            expanded.append(url+"\n")

            

    wikifile.close()
    MyFile=open('ExpandedListNews.txt','w')
    MyFile.writelines(expanded)
    MyFile.close()
    return tempicount

search_terms_file=open('movie_terms.txt','r')
query_list = search_terms_file.read().splitlines()
query_test = ["Modi", "loan", "honey"]
icount = 0
for i in range(len(query_test)):
    icount = writeToCSV(query_test[i], icount)

