# BPE for all Shakespeare text on Gutenberg.org
# define imports
import requests
import numpy as np
import re

# links to all of Shakespeare, lucky for me the complete works is in one txt file
shakespeare_txt_lnk = "https://www.gutenberg.org/cache/epub/100/pg100.txt"
shakespeare_txt = requests.get(shakespeare_txt_lnk).text
# assert isinstance(shakespeare_txt, text)
print(shakespeare_txt)
