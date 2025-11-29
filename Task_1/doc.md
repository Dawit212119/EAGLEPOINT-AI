# Text Analyzer Documentation

## Overview
The `text_analyzer.py` script provides a utility function `analyze_text` that performs statistical analysis on a given input string. It identifies words, handling specific delimiters and punctuation, and calculates metrics such as word count, average length, and frequency.

## Function: `analyze_text(text)`

### Parameters
- `text` (str): The input string to be analyzed.

### Returns
A dictionary containing the following keys:
- `word_count` (int): The total number of valid words found.
- `average_word_length` (float): The average length of the words, rounded to 2 decimal places.
- `longest_words` (list): A list of the longest words found (case-sensitive).
- `word_frequencies` (dict): A dictionary mapping lowercased words to their occurrence count.

If an error occurs (e.g., invalid input type), it returns a dictionary with an `"error"` key.

### Logic Details
1. **Input Validation**: Checks if the input is a string. Returns an error message if not.
2. **Preprocessing**: 
   - Handles consecutive apostrophes (e.g., `''`) by replacing them with a space.
   - Splits the text by colons (`:`) or commas (`,`) to separate potential segments.
3. **Tokenization**: Uses a regular expression `\b\w+(?:['-]\w+)*\b` to identify words. This pattern supports:
   - Standard alphanumeric words.
   - Words with internal hyphens (e.g., `foo-bar`).
   - Words with internal apostrophes (e.g., `café's`).
4. **Statistics**:
   - **Word Count**: Total number of tokens.
   - **Average Length**: Sum of lengths divided by count.
   - **Frequency**: Counts occurrences (case-insensitive).
   - **Longest Words**: Finds words with the maximum length. Uniqueness is determined by the lowercase version, but the original casing is preserved in the output list.

### Example Usage

```python
text = "The quick brown fox jumps over the lazy dog"
result = analyze_text(text)
print(result)
```

**Output:**
```json
{
    "word_count": 9,
    "average_word_length": 3.89,
    "longest_words": ["quick", "brown", "jumps"],
    "word_frequencies": {
        "the": 2,
        "quick": 1,
        "brown": 1,
        "fox": 1,
        "jumps": 1,
        "over": 1,
        "lazy": 1,
        "dog": 1
    }
}
```

