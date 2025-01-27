# Import
import spacy

print('Keywords')
# Keywords
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print('Tokenization')

# Tokenization
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

print('Sentences')

# Sentences
sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

print('My Example')
# My own example(Lion, Elephant and potatoes)
example_tokens = nlp('Lion Elephant Potatoes')

for token in example_tokens:
    for token2 in example_tokens:
        print(token.text, token2.text, token.similarity(token2))




