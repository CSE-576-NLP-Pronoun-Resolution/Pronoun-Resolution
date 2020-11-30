# Fine Tuning HuggingFace-Transformers

This folder contains notebooks to Finetune HuggingFace implementations of BERT and RoBerta. The weights of the models were frozen then two Neural Layers were attached to the same before training.
The architecture of the Neural Network attached is shown below.

Both the models were trained for 25 epochs with 100% of Collected Data and 20% of [WinoGrande dataset](https://winogrande.allenai.org/). The models were tested on the rest 80% of WinoGrande dataset.

![](FineTuneNN.png)



