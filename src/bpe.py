# this will be a second, better rendition of the first_bpe that I made
# the first version is slow and relies on thousands of for loops
# i looked around and found a library called collections that will enable a count in one pass
import unicodedata
from collections import Counter
from itertools import pairwise  # using pairwise in place of zip()


def get_max_pair(ids):
    """Finds the most common pairs in a dataset, returns said pair."""
    return Counter(pairwise(ids)).most_common(1)[0][0]

def replace_w_pair(ids, pair, new_id): # need new_id 
    """Replace pairs at idx, idx+1 with pair from get_max_pair."""
    # empty list for new chars and index to not supercede len(chars)
    new_ids, idx = [], 0
    while idx < len(ids):
        # find the pairs to replace
        if ids[idx] == pair[0] and idx+1 < len(ids) and ids[idx+1] == pair[1]:
            new_ids.append(new_id)
            idx += 2 # skip 2 places since we are replacing two chars with 1

        else:
            new_ids.append(ids[idx])
            idx += 1

    return new_ids

def excl_control_chars(chars: str) -> str:
    """Function to remove control characters on text output."""
    clean_chars = []

    for char in chars:
        # "C" stands for other characters in unicodedata that you don't want messing wity your ouptut text
        if unicodedata.category(char)[0] != "C":
            clean_chars.append(char)
        else:
            # append the char's escape frequenc
            clean_chars.append(f"\\u{ord(char):04x}")
    # return the chars joined together
    return "".join(clean_chars)


def return_token_pretty(tokens: bytes) -> str:
    """Returns a human-readable token!"""
    # decode token bytes to utf-8
    words = tokens.decode("utf-8", errors='replace') # returns replacement error instead of crashing. default='strict'
    words = excl_control_chars(words)
    return words


# simple tokenizer that encodes or decodes our text from new vocab
class Tokenizer:
    """Encodes or Decodes vocab after BPE. Or whenever you want, if you're just curious."""

    def __init__(self,) -> None:
        # merges is a dict of what merged tokens became and their new index
        self.merges = {}
        # vocab is what each number means in subword form (ex: 116: "t")
        self.vocab = {i:bytes([i]) for i in range(256)}

    def encoder(self, text: str) -> list[int]:
        """Encode text into BPE token ids"""
        # convert text to a list: utf-8
        ids = list(text.encode("utf-8"))
        # not including ids less than two items long, they won't be able to pair that way
        while len(ids) >= 2:
            pairs = set(pairwise(ids))
            # pair
            pair = min(pairs, key=lambda p: self.merges.get(p, float("inf")))

            if pair not in self.merges:
                break

            ids = replace_w_pair(ids, pair, self.merges[pair])
        return ids

    def decode(self, ids) -> str:
        """Decodes a string into the token indices values defined in our vocab."""
        tokens = b"".join(self.vocab[idx] for idx in ids)
        return tokens.decode("utf-8", errors="replace")
    
    def train(self, data: bytes, vocab_size: int):
        """Takes in data, creates the merges, appens to vocab."""
        # bring in the bytes as a list to loop over
        ids = list(data)
        # since the first 256 of the vocab were already assigned, we subtract 256 for each loop
        for i in range(vocab_size - 256):
            if len(ids) < 2:
                break
            # loop through the ids and find the most frequently occuring pair
            pair = get_max_pair(ids) 
            idx = 256+i
            # replace every occurence of the two chars that make the pair, replacing with pair at first index
            ids = replace_w_pair(ids, pair, idx)
            self.merges[pair] = idx
            # append to vocab dict then merged pairs
            self.vocab[idx] = self.vocab[pair[0]] + self.vocab[pair[1]]






