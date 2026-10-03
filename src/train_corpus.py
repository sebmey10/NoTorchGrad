# train a corpus of text, output to dataset

import requests

from src.bpe import Tokenizer
from src.cleantxt import CleanText

url = "https://www.gutenberg.org/cache/epub/1952/pg1952.txt"

response = requests.get(url)
response.raise_for_status()

text = response.text

data = CleanText.clean_text(text)

tokenizer = Tokenizer()

tokenizer.train(data=data, vocab_size=500)



