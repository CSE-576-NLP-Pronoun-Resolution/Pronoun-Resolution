News Article Dataset Generator

A dataset generator to extract sentences from news articles on NYTimes. The contents of the articles are scanned and using HTML parser, specific tags are copied into a .csv file. Some data cleaning processes are involved such as tags separation, deletion of unnecessary tags. The implementation is in  Python 3. The output is a .csv file. The format of the file is as follows:

Article title, content, link

APIs used - NYTimes News Article
Modules to be installed - BeautifulSoup

Instructions to run:

1. Empty the ExpandedListNews.txt and news_article.csv file
2. Run the newsarticle_dataset.py
Adjust the max article size according to system performance.

