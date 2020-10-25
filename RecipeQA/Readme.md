# RecipeQA filtering
## Description

Extract sentences from the RecipeQA dataset (https://hucvl.github.io/recipeqa/) and use adjustable filters to generate valid data for pronoun resolution.

The following filters are used:
- Sentence chunking to determine the number of noun phrases in each sentence. Only sentences with at least three noun phrases are collected (A, B, pronoun)
- Part-of-speech tagging to determine which pronouns (if any) appear in each sentence. Samples are only collected if they contain only one pronoun. For this dataset, only the pronouns 'it', 'them', and 'they' are accepted. However, only 'it' sentences were included for the synthetic data generation task.
- Remove irrelevant punctuation from sentences. Remove text inside parentheses and other punctuation that is not important towards the meaning of the sentence.

Other filters which were included for evaluation, but were not used for the final synthetic data generation, are:
- Only collect samples containing exactly three noun phrases
- Use POS tagging to determine the location of the nouns and only collect sentences in which the two nouns are antecedents (appear before the pronoun)

## Running the code
Download the RecipeQA train data. Set `input_file_path` to the path of the JSON file. Optionally, set `output_file_path` to the file in which you would like to save the filtered sentences.
