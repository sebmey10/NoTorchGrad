# This will be the Byte Pair Encoding portion where I loop through IDK let's just do 1000 times for fun
# We can experiment later with different amounts

# imports
# import numpy as np

# from cleantxt import CleanText
# from src import cleantxt

# define the text constant I need to loop through from cleantxt.py
# SHAKESPEARE_TXT = cleantxt.shakespeare_txt
# SHAKESPEARE = CleanText.clean_text(SHAKESPEARE_TXT)


# set up the BPE class 
class BPE:
    """Performs Byte Pair Encoding on text."""    
    # def __init__(self, text: str):
    #     self.text = text

    # third, I will define the loop for the text
    @staticmethod    
    def bpe_loop(text: str, n_loop: int = 10000) -> list:
        """Takes in text, loops over it default 1000 times and returns the new vocab.

        Args:
            text: imported text to loop over.
            n_loop: number of loops we are going to perform BPE.
        
        Returns:
            list: f vocab + new subwords."""
        
        tokens = [tok for tok in text] # vocab starts off as each token in text
        pairs = [] # append pairs here, will need to delete at beginning of next loop
        for i in range(n_loop): # loop 1000 times

            for idx in range(len(tokens) -1 ): # this is being changed every loop
                pair = tokens[idx] + tokens[idx+1] 
                pairs.append(pair)

            # need a way to count all the pairs and return the pair that occurred most
            # going to use max(pairs, key=pairs.count)
            high_freq_pair= max(pairs, key=pairs.count)
        
            # now, we need to walk through the text again and replace the neighboring
            # tokens that equaled high_freq_pair and replace them with high_freq_pair
            # we will make a new list called new_tokens that will replace tokens because
            # it will have the replaced values
            new_tokens = []
            
            idx = 0
            while idx < len(tokens):
                if idx+1 < len(tokens) and tokens[idx] + tokens[idx+1] == high_freq_pair:
                    new_tokens.append(high_freq_pair)
                    
                    # now we need to ensure that idx doesn't start at the next value
                    # because we don't want to append idx+1
                    idx += 2
                
                else:
                    new_tokens.append(tokens[idx])
                    idx += 1
        
            tokens = new_tokens

            pairs.clear()
            
        return tokens






                


