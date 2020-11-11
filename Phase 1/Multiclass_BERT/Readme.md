# Multiclass classification with BERT

Before training the classifier, the training set is preprocessed and a label is assigned to each sample. The label indicates which noun the pronoun refers to in the following manner:
  - **0** if the pronoun refers to A
  - **1** if the pronoun refers to B
  - **2** if the pronoun refers to neither A nor B

Then, the model is trained on this data. The `bert-base-cased` model was found to provide the best results. We used the cased model because for this task, casing may provide important information in the case of proper nouns.

When testing the model on our dataset, we used a 60%/20%/20% split for train, validation, and test data. When testing on a separate dataset, we used a 80%/20% split on our dataset for train and validation data.

## Running the code

Before running `Multiclass_BERT.ipynb`, download our dataset from [this link](https://github.com/CSE-576-NLP-Pronoun-Resolution/Pronoun-Resolution/blob/master/Dataset/Dataset.csv). For testing, also download the [GAP coreference test dataset](https://github.com/google-research-datasets/gap-coreference). In `Multiclass_BERT.ipynb`, edit the paths for label_df and gap_df so that they point to the location of their corresponing files.
  
---  
## Results

**Table 1:** Test results on our dataset
|  | precision | recall | f1-score | support | 
|--|--|--|--|--|
| 0 | 0.9060 | 0.8942 | 0.9001 | 851 |
| 1 | 0.7008 | .7713 | 0.7344 | 328 |
| 2 | 0.6591 | 0.4394 | 0.5273 | 66 |
|  |  |  |  |  |
| accuracy |  |  | 0.8378 | 1245 |
| macro avg| 0.7553 | 0.7017 | 0.7206 | 1245 |
| weighted avg | 0.8388 | 0.8378 | 0.8367 | 1245 |

<br>
<br>

**Table 2:** Test results on GAP coreference dataset
|  | precision | recall | f1-score | support | 
|--|--|--|--|--|
| 0 | 0.5009 | 0.6394 | 0.5617 | 918 |
| 1 | 0.4990 | .2947 | 0.3706 | 855 |
| 2 | 0.1889 | 0.0.2687 | 0.2218 | 227 |
|  |  |  |  |  |
| accuracy |  |  | 0.4500 | 2000 |
| macro avg| 0.3962 | 0.4010 | 0.3847 | 2000 |
| weighted avg | 0.4647 | 0.4500 | 0.4414 | 2000 |
