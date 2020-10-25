Context Based True Labelling for Pronoun

The code in RecipeQA_it_context_check, finds the true labels based on the context of the text. Sentences with 'it' pronoun are filtered and given true labels using QA models and the context as information.

Algorithm used:
Step 1: take a sentence/step, check if the sentence/step contains the pronoun 'it'.
Step 2: If the sentence/step had an 'it' we will try to resolve it using the Q/A model.
Step 3: If not resolved, then combine the previous sentence/step and pass it as info for the Q/A model.
Step 4: Repeat step 3, with a previous sentences/steps, untill 'it' can be resolved.
step 5: Repeat steps 1 - 4 for all sentences/steps.

Step 1:
The processed RecipeQA dataset is taken. The text is sepearated into steps and the sentences in the steps are generated into a list.
Sample structure:
Text: {
  step_1: [sentence_1, sentence_2, sentence_3....,sentence_n],
  step_2: [sentence_1, sentence_2, sentence_3....,sentence_n],
  step_3: [sentence_1, sentence_2, sentence_3....,sentence_n],
  ....
  step_n: [sentence_1, sentence_2, sentence_3....,sentence_n],
}
Using POS tagger the parts of speecch in the sentences are predicted and the sentences with the it will taken.

Step 2:
The extracted sentence is sent to QA model. If not able to resolve the it with the current text step 3 is executed.

example:
"make sure to wrap it nice and tight so the pepper can't slip out or open up."
The "it" in this sentence is not pointing to any noun before it.

Step 3:
The previous sentence is combined to the current sentence and then sent to the QA model.

Current Sentence: "make sure to wrap it nice and tight so the pepper can't slip out or open up."
Previous Sentence: "Take a long, thinly sliced piece of prosciutto and wrap it around each stuffed jalapeño separately."
Combined Sentence: "Take a long, thinly sliced piece of prosciutto and wrap it around each stuffed jalapeño separately, make sure to wrap it nice and tight so the pepper can't slip out or open up."

Step 4:
After combining the sentence, the QA model can find the answer based on the extra information provided.

Answer: prosciutto
