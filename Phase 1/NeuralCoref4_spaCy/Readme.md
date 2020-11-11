# NeuralCoref 4.0: Coreference Resolution in spaCy with Neural Networks.

To run the Coref_Analysis.ipynb, run each block separately. 
- Copy files from git to Google Drive. 
- Copy the authorization code to allow gdrive access. 
	The .csv files used can be found in git as follows:
		1. gap-test.tsv ---> https://github.com/google-research-datasets/gap-coreference
		2. Cleaned_Dataset ---> https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Dataset
- Install all the necessary packages as given in notebook file.
- The file will generate output for the two testing dataset.

The model generated the following results:

<br>
**Table 1:** Test results 

-----------------------------------------------------------------------------------------
| Dataset 	| Accuracy	| Pronoun Offset 	| Coref A 	| Coref B 	| 
|---------------|---------------|-----------------------|---------------|---------------|
| Our Dataset 	| 0.5153 	| 51.4352 		| 0.6616 	| 0.3383 	|
| Gap Dataset 	| 0.3145 	| 330.151 		| 0.459 	| 0.4275 	|
-----------------------------------------------------------------------------------------

The results included some false negatives by the NeuralCoref model such as in the CleanedDataset.csv file, refer to ID = 12, the pronoun 'he' refers to D'Annunzio, our dataset also has the correct coreference resolution. But the neuralcoref predicts 'he' refers to De. Which is a False Negative. 
Another important issue analysed in this activity is that, the neuralcoref predicts too specific nouns. Example, refer to ID = 3, the noun 'he' refers to "young Norris" according to the neuralcoref model. An answer like "Norris" is not wrong, but less specific. It is not exactly a False Negative but a strict equals while comparing strings, would flag this as a false positive. 
These are some issues analysed in the testing of neuralcoref model. 