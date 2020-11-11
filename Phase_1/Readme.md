# Pronoun Resolution - Phase 1 Results

Specific instructions to run the files will be available in respective directories. Here are the analysis with several models that we tried out with respective to our dataset available at https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Dataset and https://github.com/google-research-datasets/gap-coreference/

src available at https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Phase_1

____________________________________________________________________________________________________________________________________

# Data Validation with NeuralCoref 4.0: Coreference Resolution in spaCy with Neural Networks

Git repo -------> https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Phase_1/NeuralCoref4_spaCy

The collected dataset was validated using NeuralCoref 4.0 and the quality of the dataset was gauged with respect to NeuralCoref 4.0. The accuracy for our dataset was approximately 51.53% while the same with Google's dataset was 31.45%. The error was mostly due to the presence of more than one pronoun referencing to multiple objects.

The results included some false negatives by the NeuralCoref model such as in the CleanedDataset.csv file, refer to ID = 12, the pronoun 'he' refers to D'Annunzio, our dataset also has the correct coreference resolution. But the neuralcoref predicts 'he' refers to De. Which is a False Negative. 

Another important issue analysed in this activity is that, the neuralcoref predicts too specific nouns. Example, refer to ID = 3, the noun 'he' refers to "young Norris" according to the neuralcoref model. An answer like "Norris" is not wrong, but less specific. It is not exactly a False Negative but a strict equals while comparing strings, would flag this as a false positive. 
These are some issues analysed in the testing of neuralcoref model. 


Table 1: Data Validation Results


| Dataset 	| Accuracy	| Pronoun Offset 	| Coref A 	| Coref B 	| 
|---------------|---------------|-----------------------|---------------|---------------|
| Our Dataset 	| 51.53% 	| 51.4352 		| 66.16% 	| 33.83% 	|
| Gap Dataset 	| 31.45% 	| 330.151 		| 45.9% 	| 42.75% 	|


- Dataset -> Dataset used according to the links given above
- Accuracy -> Number of correctly resolved pronouns / Cardinal number in dataset
- Pronoun Offset -> Average index position of pronoun in the context
- Coref A -> Number of times coreference A returned true for the pronoun resolution
- Coref B -> Number of times coreference B returned true for the pronoun resolution

____________________________________________________________________________________________________________________________________

# Multiclass classification with BERT

Git repo -------> https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Phase_1/Multiclass_BERT

Before training the classifier, the training set is preprocessed and a label is assigned to each sample. The label indicates which noun the pronoun refers to in the following manner:
  - **0** if the pronoun refers to A
  - **1** if the pronoun refers to B
  - **2** if the pronoun refers to neither A nor B

Then, the model is trained on this data. The `bert-base-cased` model was found to provide the best results. We used the cased model because for this task, casing may provide important information in the case of proper nouns.
When testing the model on our dataset, we used a 60%/20%/20% split for train, validation, and test data. When testing on a separate dataset, we used a 80%/20% split on our dataset for train and validation data.

____________________________________________________________________________________________________________________________________

# Transformers and Classifiers - BERT, RoBERTa and GloVe

Git repo -------> https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/tree/master/Phase_1/Transformers_and_Classifiers

We have used some transformer models to compute the contextual embedding of the pronoun and two possible candidates(let’s call them A and B) it may refer to. After obtaining the embeddings, they are used to classify into three labels ‘A’, ‘B’ and ‘Neither’. Different types of transformers-based models were used to compute the embeddings, they are tabulated below in table 1.0 with their accuracies.
In Contextual_Embeddings_usingBERT.ipynb, we aim to learn the contextual embeddings for the Pronoun, and its possible resolutions from the sentence and frame the Pronoun resolution task as a Supervised Classification task.

All the models were tested with the GAP dataset to compare their performance. Tabulated as follows:


____________________________________________________________________________________________________________________________________

# Overall Results of Various Models

Table 2: Analysis with various models


| Method Used				| Created Dataset (TRAIN + TEST)| GAP Dataset (TEST)	| 
|--					|--				|--			|
| Multiclass BERT classification	| 83.7% 			| 45%	 		|
| Roberta +  XGBoost Classifier		| 79.7% 			| 56.25% 		|
| BERT Embeddings + XGBoost Classifier	| 77.78% 			| 55%	 		|
| GloVe + XGBoost Classifier		| 68.2% 			| 37.2% 		|

