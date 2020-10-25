from flair.models import SequenceTagger
from flair.data import Sentence
from nltk import tokenize
import pandas as pd
from tqdm import tqdm
import json
import re
import nltk

def filter_sentences(file_path: str, start_index: int, end_index: int):
    nltk.download('punkt')
    chunk_tagger = SequenceTagger.load('chunk')
    pos_tagger = SequenceTagger.load('pos')

    # json_data=open("/content/drive/My Drive/NLP/recipeqa/train.json")
    json_data = open(file_path)
    jdata = json.load(json_data)

    par = []
    for obj in jdata['data']:
        for context in obj['context']:
            text = context['body'].lstrip()
            if text:
                text = re.sub(r'(?<=[.,!])(?=[^\s])', r' ', text)
                par.append(text)

    # Remove parenthesis and other punctuation that does not add to the text
    par_cleaned = []
    for p in par:
        if '(' in p and ')' in p:
            p_cleaned = re.sub(r" ?\([^)]+\)", "", p)
        elif '[' in p and ']' in p:
            p_cleaned = re.sub(r" ?\[[^)]+\]", "", p)
        elif '{' in p and '}' in p:
            p_cleaned = re.sub(r" ?\{[^)]+\}", "", p)
        else:
            punc = "`~@#^&*<>=+_()[]{}|"
            p_cleaned = p
            for ch in p:
                if ch in punc:
                    p_cleaned = p_cleaned.replace(ch, '')
        par_cleaned.append(p_cleaned)

    raw_sentences = [tokenize.sent_tokenize(p) for p in par_cleaned]
    raw_sentences = [item for sublist in raw_sentences for item in sublist]

    sent_final = []
    for sent in raw_sentences:
        if sent[0].isalpha():
            sent_final.append(sent)

    print("Total sentences: {}".format(len(sent_final)))
    # Adjust the number based on how many samples to start with
    raw_sentences = sent_final[start_index:end_index]

    print("{} sentences loaded".format(len(raw_sentences)))

    # Tokenize sentences
    print('Tokenizing sentences for filter 1')
    sentences = [Sentence(s) for s in raw_sentences]

    # Chunking the sentences into phrases
    print("Chunking sentences")
    chunk_tagger.predict(sentences)

    # Count the number of noun phrases. There should be at least 3 (A, B, pronoun)
    print("\nApplying filter 1")
    filter1_sentences = []
    for sent in tqdm(sentences):
        if [chunk.tag for chunk in sent.get_spans()].count('NP') >= 3:
            filter1_sentences.append(sent.to_original_text())

    print('\nFilter 1: Removed {} sentences'.format(len(sentences) - len(filter1_sentences)))

    # Tokenize the filtered sentences again to clear existing tags
    print("Tokenizing sentences for filter 2")
    sentences = [Sentence(s) for s in filter1_sentences]

    # POS tagging
    print("Tagging sentences with POS")
    pos_tagger.predict(sentences)

    # Only take sentences with "it" or "them" as the pronoun
    print("\nApplying filter 2")
    filter2_sentences = []
    for sent in tqdm(sentences):
        token_list = [token.text for token in sent]
        if (token_list.count('it') + token_list.count('them') + token_list.count('they') == 1) and [
            token.get_tag('pos').value for token in sent].count('PRP') == 1:
            filter2_sentences.append(sent.to_original_text())

    print('\nFilter 2: Removed {} sentences'.format(len(sentences) - len(filter2_sentences)))

    # Tokenize the filtered sentences again to clear existing tags
    print("Tokenizing sentences for filter 3")
    sentences = [Sentence(s) for s in filter2_sentences]

    # # Filter 3: Only include samples in which there are 2 ANTECEDENTS
    # print("\nApplying filter 3")
    # filter3_sentences = []

    # for sent in tqdm(sentences):
    #     sent_chunk = sent
    #     chunk_tagger.predict(sent_chunk)
    #     NP_start_indices = []
    #     for entity in sent_chunk.get_spans():
    #         if entity.tag == 'NP':
    #           NP_start_indices.append(entity.start_pos)

    #     sent_pos = sent
    #     pos_tagger.predict(sent_pos)
    #     POS_start_index = 0
    #     for token in sent_pos:
    #         if token.get_tag('pos').value == 'PRP':
    #             POS_start_index = token.start_pos

    #     if NP_start_indices[0] < POS_start_index and NP_start_indices[1] < POS_start_index:
    #         filter3_sentences.append(sent.to_original_text())
    filter3_sentences = filter2_sentences
    print('\nSentences after filtering: {}'.format(len(filter3_sentences)))

    # Save 'it' sentences to file
    it_sentences = []
    # Replace 'filter3_sentences' with wiki_sentences if using wiki dataset
    for sent in filter3_sentences:
      if 'it' in sent.split():
        it_sentences.append(sent)

    return it_sentences

 input_file_path = 'recipeqa/train.json'
 output_file_path = 'output/recipeqa_filtered_sent.csv'

filtered_sent = filter_sentences(input_file_path, 0, 20)
sent_df = pd.DataFrame(filtered_sent, columns=['sentence'])

sent_df.to_csv(output_file_path)
