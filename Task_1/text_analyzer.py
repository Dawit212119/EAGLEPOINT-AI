import re
from collections import Counter

def analyze_text(text):
    try:
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        if not text.strip():
            return {
                "word_count": 0,
                "average_word_length": 0,
                "longest_words": [],
                "word_frequencies": {}
            }

        #  Replace multiple consecutive apostrophes with a space
        text = re.sub(r"'{2,}", " ", text)

       
        # Split on colon or comma
        parts = re.split(r"[:,]", text)

        
        # matches letters/digits/Unicode, single internal apostrophes, hyphens
        pattern = r"\b\w+(?:['-]\w+)*\b"

        words = []
        for part in parts:
            words.extend(re.findall(pattern, part, flags=re.UNICODE))

        if not words:
            return {
                "word_count": 0,
                "average_word_length": 0,
                "longest_words": [],
                "word_frequencies": {}
            }

        
        word_count = len(words)
        avg_length = round(sum(len(w) for w in words) / word_count, 2)

        
        frequency = Counter(w.lower() for w in words)

        
        max_len = max(len(w) for w in words)
        seen = set()
        longest = []
        for w in words:
            lw = w.lower()
            if len(w) == max_len and lw not in seen:
                longest.append(w)
                seen.add(lw)

        return {
            "word_count": word_count,
            "average_word_length": avg_length,
            "longest_words": longest,
            "word_frequencies": dict(frequency)
        }

    except TypeError as te:
        return {"error": str(te)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}



# text = "'dfd' ''foo  bar' foo-bar foo'bar foo''bar ''foo ''foo'' café's pizza:bread:burger"
# print(analyze_text(text))

text="The quick brown fox jumps over the lazy dog the fox" 
print(analyze_text(text))

# print(analyze_text("'dfd' ''foo  bar' foo-bar foo'bar'"))
# print(analyze_text("11 22 33 11 22 11' 33')()"))
# print(analyze_text(text))
# print(analyze_text(12345))  
# print(analyze_text(""))  
# print(analyze_text("!!! ??? ... ;;::--''")) 

# print(analyze_text("-dff- "))
# print(analyze_text("---dff--- "))

