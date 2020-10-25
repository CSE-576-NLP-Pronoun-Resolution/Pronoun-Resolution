To find the true label for the sentences in the generated dataset, we use DeepPavlov’s [1]  Question Answering model that was trained on Stanford Question Answering Dataset.

For each sentence in the extracted data, we pass the sentence along with a question that is crafted specifically such that by answering the question we are indirectly resolving the pronoun that is found. 

Solving for Pronouns He and She:
To solve these pronouns in the sentences, we have to target the nouns that are persons for sure. Therefore we define “Who” questions that are followed by the context referenced by the pronoun. These types of questions are able to find nouns that correspond to the pronoun. 
 
For example:

Text: “After the war, Herbert attended the University of Washington, where he met Beverly at a creative writing class in 1946 .”

Question: “Who met Beverly at a creative writing class in 1946?”
Answer: “Herbert”

Solving the ‘It’ pronoun:

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

Question: “What  on top butter side up. ?”
Answer: “bread”

Final Answer: “bread”

Reference: 
http://docs.deeppavlov.ai/en/master/features/models/squad.html
