from src.bpe import BPE
from src.cleantxt import CleanText, shakespeare_txt

# this is a test script to see, first, if I return a valid list of pairs from BPE.py
test_txt = shakespeare_txt

cleaned_txt = CleanText.clean_text(test_txt)

bpe = BPE.bpe(text=cleaned_txt, n_loop=10)

# printing all of the merges that we find in 10 loops
assert isinstance(bpe, list)
