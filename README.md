CSE 576 - NLP
Pronoun Resolution
Submitted to Dr. Chitta Baral

Group Members:
1. Aparokshith Rao (asrao13@asu.edu)
2. Sanjay Arivazhagan (sarivazh@asu.edu)
3. Siddharth Rawal (sidrawal@asu.edu)
4. Sethu Manickam (smanick4@asu.edu)

Mentor:
1. Pratyay Banerjee (pbanerj6@asu.edu)




---------------------------------------------------------------------------------------------------------------------------------------------
Git Link to Final Dataset	----------->
---------------------------------------------------------------------------------------------------------------------------------------------
https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/blob/master/Dataset/Dataset.csv
OR
https://drive.google.com/file/d/14a4sekDkTEV0KRLvU-NwYEmOgS9nFQVV/view?usp=sharing



---------------------------------------------------------------------------------------------------------------------------------------------
Columns in the Dataset	----------->
---------------------------------------------------------------------------------------------------------------------------------------------
 _______________________________________________________________________________________________________________________________________
|Column	|	Header		|	Description											|
|-------|-----------------------|-------------------------------------------------------------------------------------------------------|
|1.	|	Text		|	The sentence or context containing pronoun to be resolved with 2 or more candidate names.	|
|2.	|	Pronoun		|	The pronoun to be resolved									|
|3.	|	Pronoun-offset	|	Character offset of the pronoun in Text								|
|4.	|	Answer		|	The candidate that the Pronoun refers to							|
|5.	|	Answer-offset	|	Character offset of the Answer in Text								|
|6.	|	Possible anwers	|	List of all possible candidate names described in 1						|
|_______|_______________________|_______________________________________________________________________________________________________|






---------------------------------------------------------------------------------------------------------------------------------------------
Tasks Assigned 		----------->
---------------------------------------------------------------------------------------------------------------------------------------------



1. Aparokshith Rao (asrao13@asu.edu)

Worked on finding true label and its analysis. 

A) He/She (Personal Pronoun), and It Question Generation		- To solve these pronouns in the sentences, we have to target the nouns that are persons for sure. Therefore we define “Who” questions that are followed by the context referenced by the pronoun. These types of questions are able to find nouns that correspond to the pronoun. 

For example:
Text: “After the war, Herbert attended the University of Washington, where he met Beverly at a creative writing class in 1946 .”

Question: “Who met Beverly at a creative writing class in 1946?”
Answer: “Herbert”

The correct answer corresponding to it/it’s could either be a noun or a proper noun in its singular or plural form. So it is important to frame the question that takes into account these factors. We devise a vote based question and answering method to find out the exact true label corresponding to the pronoun.  

The questions are created as follows:
“What is” +  past_tense(ROOT)
“What is”+ past_tense(conjunct(s) found)
“What is” + the context after the pronoun
“What” + the context after the pronoun

Before the questions are posed against the said text, we extract the possible candidates for the corresponding pronoun, essentially making this a multiple-choice question. The final answer is the answer with the majority vote.

For example:
Text: “Butter another slice of bread and place it on top butter side up.”

Question: “what is Butterred ?”
Answer: “another slice of bread”


Question: “what is placed ?”
Answer: “Butter”

Question: “What is  on top butter side up. ?”
Answer: “bread”

Final Answer: “bread”

[Git Link - https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/He_She_Pronoun_Data]



B) QA Model and Final Data Generation				- All the sentences (Text) is appened into a single CSV file, and the same is passed in as input to the QA model. Similarly, all the questions generated for 'it' pronouns, 'he' and 'she' pronouns are also appended corresponding to the Text in the Text CSV file. To find the true label for the sentences in the generated dataset, we use DeepPavlov’s [1]  Question Answering model that was trained on Stanford Question Answering Dataset.
For each sentence in the extracted data, we pass the sentence along with a question that is crafted specifically such that by answering the question we are indirectly resolving the pronoun that is found. 



---------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------


2. Sanjay Arivazhagan (sarivazh@asu.edu)

A) Wikipedia Crawler and News Article Dataset Collection	- A crawler to move between selected wikipedia articles.The contents of the articles are scrapped removing unwanted sections such as references, see also. The implementation is done in python3. The output of the scrapper is put in a .csv file in the format below.

	- Article title, content, link

	- API used: Wikipedia (Python)
	- The code is written for python3 version
	- Python3 modules to be installed: Spacy Wikipedia

[Git - https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Wikipedia_Crawler]

B) Context Based True Labelling for Pronoun - The code in RecipeQA_it_context_check, finds the true labels based on the context of the text. Sentences with 'it' pronoun are filtered and given true labels using QA models and the context as information.

- Algorithm used:
	- Step 1: take a sentence/step, check if the sentence/step contains the pronoun 'it'.
	- Step 2: If the sentence/step had an 'it' we will try to resolve it using the Q/A model.
	- Step 3: If not resolved, then combine the previous sentence/step and pass it as info for the Q/A model.
	- Step 4: Repeat step 3, with a previous sentences/steps, untill 'it' can be resolved.
	- Step 5: Repeat steps 1 - 4 for all sentences/steps.

	- Step 1:
		The processed RecipeQA dataset is taken. The text is sepearated into steps and the sentences in the steps are generated into a list.
		Sample structure:
		Text: {
		  step_1: [sentence_1, sentence_2, sentence_3....,sentence_n],
		  step_2: [sentence_1, sentence_2, sentence_3....,sentence_n],
		  step_3: [sentence_1, sentence_2, sentence_3....,sentence_n],
		  ....
		  step_n: [sentence_1, sentence_2, sentence_3....,sentence_n],
		}
	- Using POS tagger the parts of speecch in the sentences are predicted and the sentences with the it will taken.

	- Step 2:
		The extracted sentence is sent to QA model. If not able to resolve the it with the current text step 3 is executed.

		example:
		"make sure to wrap it nice and tight so the pepper can't slip out or open up."
		The "it" in this sentence is not pointing to any noun before it.

	- Step 3:
		The previous sentence is combined to the current sentence and then sent to the QA model.

		Current Sentence: "make sure to wrap it nice and tight so the pepper can't slip out or open up."
		Previous Sentence: "Take a long, thinly sliced piece of prosciutto and wrap it around each stuffed jalapeño separately."
		Combined Sentence: "Take a long, thinly sliced piece of prosciutto and wrap it around each stuffed jalapeño separately, make sure to wrap it nice and tight so the pepper can't slip out or open up."

	- Step 4:
		After combining the sentence, the QA model can find the answer based on the extra information provided.

		Answer: prosciutto

[Git Link - https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/It_Pipeline]


---------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------


3. Siddharth Rawal (sidrawal@asu.edu)

A) Recipe QA Dataset Analysis and Processing			- 
- Collect sentences from the RecipeQA dataset and determine how stringent the filters should be for the data. 
- There must be a balance between the strictness of the filters and the variation of the resulting data.
- Loose filters will allow for more variation between the filtered sentences, but the QA model used to generate true labels may not be able to label correct nouns as consistently.
- On the other hand, strict filters will result in more consistently accurate true labels, but may cause the resulting data to be more homogenous. This could prevent our pronoun resolution model from learning enough information about the various cases in which pronouns could appear, causing the model to underfit.
- Loose filters include:
	- At least 3 noun phrases in the sentence
	- One or more pronouns in the sentence
	- Several types of pronouns accepted ("he", "she", "it", "them", "they", etc.) for a single dataset
- Strict filters include:
	- Exactly 3 noun phrases in the sentence
	- Only a single pronoun in the sentence
	- Small number of pronouns accepted (ex. only "he" or "she") for each dataset
	- One or both nouns must be antecedents (appearing before the pronoun)

To determine the ideal combination of filters, data was analyzed both after filtering and after true label generation.

[Git Link - https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/RecipeQA]

B) Sentence Filtration using Chunking 				- STo obtain a list of viable sentences from from various dataset, we employ the following main filters for each sentence:
	- Chunking to split the sentence into noun phrases. There should be 3+ noun phrases in a sentence (A, B, pronoun). For this, chunking was used instead of POS tagging because for phrases like "John's son", POS tagging would detect two separate nouns whereas chunking would detect one noun phrase.
	- POS tagging to find sentences with one pronoun, choosing which pronouns are accepted. One of main factors for choosing datasets was the frequency of certain pronouns in sentences. For example, RecipeQA contains more sentences containing the pronouns "it", "they", and "them" than sentences containing "he" or "she".

Since data collected from multiple sources can vary in subject, we must choose data from a range of sources to ensure that our training data can allow a model to learn information about multiple pronouns. For example, the Wikipedia data was filtered to collect sentences containing gendered pronouns ("he" and "she"), and the RecipeQA dataset was filtered with the pronoun "it" being the focus. By collecting data from various sources, we can generate more robust training data that will allow models to learn how to deal with different pronouns in varying contexts.

Other filters were also considered to replace the above steps. For example, one method for filtering without using chunking is to do the following for every sentenceencountered: 
1. Check for two or more nouns
2. For each noun, check whether it is related to the pronoun tagged (Eg. a personal pronoun indicates a proper noun)


C) Pronoun Sentence Extraction Method Analysis			- Below is a general outline of the filters that we chose for our datasets.
1. Load data from chosen dataset
2. Use NLTK sentence tokenizer to split bodies of text into sentences
3. Strip irrelevant punctuation from sentences. Remove text contained in parentheses/brackets. Preserve important punctuation such as periods, commas.
4. Use Flair chunk tagger to chunk sentences. Only sentences that contain >=3 noun phrases move on to the next filter
5. Use Flair POS tagger to determine the POS of each token. Only sentences that contain one pronoun move on to the next step.
6. Given one or more possible pronouns to accept, only select sentences that contain these pronouns (depends on dataset being filtered).
7. Merge sentences, format data, etc. These sentences will then be fed into the QA model to determine true labels for each.




---------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------

4. Sethu Manickam (smanick4@asu.edu)

Worked on dataset collection and data cleaning.

A) News Article Dataset Collection				- Used the NYTimes Article Search API to extract HTML source code of various news articles and archived articles. Prepared a search query list of over 1000 search terms with a limit of 100 articles per search result. Each search result was parsed with HTML parser using Beautiful Soup to extract URL of the article. The URLs already scanned are maintained using a map of key value pairs, where key is the web url. If the key already exists in the map, then the article is skipped. Otherwise, specifically the article.section is extracted. The text of all the div tags are stored and the data is cleaned by looking for  After successful extraction of text from the article, it is appended to the CSV file and also the notepad file which acts as the map for storing already scanned articles. The process was repeated until about 3000 articles were scanned. 

[Git Link - https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/News_Article_Dataset_Generator]

B) Movie Reviews Dataset Collection  				- Used the NYTimes Movie Reviews API to extract HTML source code of various movie reviews based on 500 search queries. Traversed the DOM tree of the HTML generated to extract the url of each article from 'results' and 'link'. If the url was never stored in the notepad file then it will be written to the CSV file and the notepad file. The difference between the two dataset collection was in traversal of the DOM tree and the major challenge being in the older review articles stored in a different format. 

[Git Link - https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Moview_Review_Dataset_Generator]

C) Data Cleaning		 				- Cleaned the data by removing all captions, unnecessary div, and advertisement button such as photo credits, img tags, initial article metadata, and the final article credits at the bottom on the page to get only the text content from the webpages. More intensive search is carried out to eliminate the tags that could potentially contain CSS information as that could lead to broken sentences. If the article scan runs into an exception such as UnicodeEncodeError or JSONDecodeError or AttributeError, the exception is handled by skipping the article. Some regular expressions are also cleaned to input a space in between sentences:

1. \s\s (double space) - one space is removed

2. \.[A-Z] (full stop followed by next sentence without a space) - a space is added between '\.' and '[A-Z]'

3. \.”[A-Z] (full stop at the end of a quotation mark included sentence) - a space is added after ." and the next sentence

4. \.“ (full stop followed by next sentence beginning with a quotation mark) - a space is added after fullstop. 


APIs used - NYTimes Article Search, NYTimes Movie Reviews (Python)

Module needed - BeautifulSoup, code generated for Python 3


---------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------------------------------------------------------




---------------------------------------------------------------------------------------------------------------------------------------------
Instructions to run the code / Environment or Packages needed	----------->
---------------------------------------------------------------------------------------------------------------------------------------------

Specific instructions will be found in the "Readme.md" files in each folder in the repository -> https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution

