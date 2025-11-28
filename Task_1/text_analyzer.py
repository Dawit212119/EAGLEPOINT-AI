import re
from collections import Counter


def analyze_text(text: str):
    words=re.findall(r"[A-Za-z0-9']+",text)

    if not words:
        return {
            "word_count":0,
            "average_word_length":0,
            "longest_words":[],
            "word_frequencies":{}
        }
    
    word_count=len(words)
    avg_length=round(sum(len(w)  for w in words)/word_count,2)

    frequency= Counter(w.lower() for w in words)
    max_len= max(len(w) for w in words)
    seen=set()
    longest=[]

    for w in words:
        lw=w.lower()
        if len(w)==max_len and lw not in seen:
            longest.append(w)
            seen.add(lw)
    return {
        "word_count":word_count,
        "average_word_length":avg_length,
        "longest_words":longest,
        "word_frequencies":dict(frequency)
    }        

text=" The quick brown fox jumps over the lazy dog. The dog barked back at the fox! "
print(analyze_text(None))