# train a corpus of text, output to dataset

import requests

from src.bpe import Tokenizer, return_token_pretty
from src.cleantxt import CleanText

url = "https://www.gutenberg.org/cache/epub/1952/pg1952.txt"

response = requests.get(url)
response.raise_for_status()

text = response.text

data = CleanText.clean_text(text)

tokenizer = Tokenizer()

tokenizer.train(data=data, vocab_size=500)


for token_id in range(256, len(tokenizer.vocab)):
    token = tokenizer.vocab[token_id]

    print(token_id, repr(return_token_pretty(token)))




