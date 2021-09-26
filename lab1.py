from nltk import sent_tokenize
from nltk import word_tokenize

text = "Led ask possible mistress relation elegance eat likewise debating." \
       " By message or am nothing amongst chiefly address. The its enable direct" \
       " men depend highly. Ham windows sixteen who inquiry fortune demands. " \
       "Is be upon sang fond must shew. Really boy law county she unable her sister. " \
       "Feet you off its like like six. Among sex are leave law built now. In built " \
       "table in an rapid blush. Merits behind on afraid or warmly."
sents = sent_tokenize(text)
print(sents)

sent = "Led ask possible mistress relation elegance eat likewise debating."
words = word_tokenize(sent)
print(words)
