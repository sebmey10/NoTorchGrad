# this will be a simple tokenizer with encoding and decoding functions 


class Tokenizer(vocab: list) -> list:
    """Takes in the vocab and outputs the tokenized values.

    Also can take in tokenized vocab and output word/subword value."""

    def __init__(self, vocab):
        self.vocab = vocab


    def encode(self, vocab) -> list:
        """Encodes vocab to token value."""
        
        encoded_vocab = {i:w for i,w in enumerate(vocab)}

        # only want to return the keys of the function (indices)

        return encoded_vocab


    def decode(self, vocab)
