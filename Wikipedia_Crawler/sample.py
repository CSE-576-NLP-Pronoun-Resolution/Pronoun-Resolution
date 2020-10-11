"""l = []
f = open('ExpandedList.txt')
lines = f.read().splitlines()
for x in lines:
	l.append(x)
print(l)"""
"""import wikipedia
l = "Alessandro Baricco"
p = wikipedia.page(l)
links = p.links
for l in links:
	k = wikipedia.search(l)
	if(len(k) == 0):
		print(l)
		break
"""

import csv
import re
"""csv_file = open('wikipedia_db.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
f = []
for row in csv_reader:
	f.append([row[0],row[1],row[2]])

for i in f:
	x = re.findall("\s\s+", i[1])
	for s in x:
		i[1] = i[1].replace(s,"\s")
print(f)
csv_filew = open('wikipedia_db_copy.csv',mode='a')
wikiwriter = csv.writer(csv_filew, delimiter=',')

for row in f:
	wikiwriter.writerow(row)"""

"""import sys
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

MyFile=open('ExpandedList.txt','r')
expanded = []
lines = MyFile.read().splitlines()
for x in lines:
	expanded.append(x+"\n")
MyFile.close()

csv_file = open('wikipedia_db.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
f = []
for row in csv_reader:
	if row[0]+"\n" not in expanded:
		expanded.append(row[0]+"\n")

MyFile=open('ExpandedList.txt','w')
MyFile.writelines(expanded)
MyFile.close()"""

import sys
maxInt = sys.maxsize

while True:
    # decrease the maxInt value by factor 10 
    # as long as the OverflowError occurs.

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

expanded = []
csv_file = open('wikipedia_db_copy.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
line_count = 0
f = []
for row in csv_reader:
	expanded.append([row[0],row[1],row[2]])

for i in expanded:
	x = re.findall("\.[A-Z]", i[1])
	for h in x:
		print(h)
		i[1] = i[1].replace(h,h[0]+" "+h[1])
#csv_filew = open('wikipedia_db_copy.csv',mode='w')
#wikiwriter = csv.writer(csv_filew, delimiter=',')
#for row in expanded:
#	wikiwriter.writerow(row)