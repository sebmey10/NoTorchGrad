# BPE for all Shakespeare text on Gutenberg.org
# define imports
import re


# all the text is imported, time to clean it

class CleanText:
    """Cleans text."""
    #PG_HEADER_PATTERN = r"\*\*\*.*?START.*?PROJECT.*?\*\*\*"
    #PG_FOOTER_PATTERN = r"\*\*\*.*?END.*?PROJECT.*?\*\*\*"
    PG_START = r"\*\*\* ?START.*?\*\*\*"
    PG_END = r"\*\*\* ?END.*?\*\*\*" 

    @staticmethod
    def remove_metadata(text: str) -> str:
        """Removes the header and footer from the text."""
        # remove the header
        start = re.search(CleanText.PG_START,text,flags=re.DOTALL | re.IGNORECASE)
        # remove the footer
        end = re.search(CleanText.PG_END,text,flags=re.DOTALL | re.IGNORECASE)

        if start and end:
            # return text betweek the end of start regex and start of end regex
            return text[start.end():end.start()]
        return text
    
    @staticmethod
    def normalize_whitespace(text: str) -> str:
        """Normalize the whitespace."""
        # sub multiple spaces for one space
        text = re.sub(r" +", " ", text)
        # remove multiple newlines for one newline
        text = re.sub(r"\n\n+", "\n\n", text)
        # take away leading and trailing whitespace
        text = text.strip()
        return text

    @staticmethod
    def remove_numbers(text: str) -> str:
        """Remove ints from the text."""
        text = re.sub(r"\d+", "", text)
        return text

    @staticmethod
    def encode_utf8(text) -> bytes:
        """Convert text to utf-8"""
        _bytes = text.encode("utf-8")
        # retun utf-8 encoded words
        return _bytes


    @staticmethod
    def clean_text(text: str) -> str:
        """Apply all cleaning operations.
        This is the method to call."""
        text = CleanText.remove_metadata(text)
        text = CleanText.remove_numbers(text)
        text = CleanText.normalize_whitespace(text)
        return text
        


