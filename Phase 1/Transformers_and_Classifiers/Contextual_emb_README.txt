In Contextual_Embeddings_usingBERT.ipynb, we aim to learn the contextual embeddings for the Pronoun, and its possible resolutions from the sentence and frame the Pronoun resolution task as a Supervised Classification task.

We obtain the contextual embeddings using different models like BERT, RoBERTa and feed these embeddings to a classifier to obtain results.

The performance of the model has been tested with GAP dataset.

BERT Embeddings + XGBoost Classifier 
With Created Dataset: Accuracy -> 77.78%
With GAP Dataset: Accuracy ->55%

RoBERTa + XGBoost Classifier
With Created Dataset: Accuracy -> 77.78%
With GAP Dataset: Accuracy ->55%
Code: https://colab.research.google.com/drive/1XNLADlBQQEWl65ABith75cs7ey5v6VNs#scrollTo=nfnSd_7M8o7K

GloVe + XGBoost Classifier
With Created Dataset: Accuracy -> 77.78%
With GAP Dataset: Accuracy ->55%
Code: https://colab.research.google.com/drive/1tDSG71vvt2R03e3ye6GhPAeokDHz1cXE#scrollTo=GUi_x2aMVxO3