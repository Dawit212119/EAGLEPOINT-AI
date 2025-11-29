# Task 1 – Smart Text Analyzer (Python) Documentation

## 1. Searches I Made (as required by the challenge)

### Google Searches

- **"python regex allow hyphens and apostrophes in words"**
  - https://www.google.com/search?q=python+regex+allow+hyphens+and+apostrophes+in+words

- **"python extract words with unicode accents regex"**
  - https://www.google.com/search?q=python+regex+unicode+accents+word+characters

- **"python split on comma and colon re.split"**
  - https://www.google.com/search?q=python+re.split+comma+colon

- **"python Counter lower case frequency"**
  - https://www.google.com/search?q=python+counter+word+frequency

### StackOverflow References

- **Regex for capturing words with apostrophes or hyphens**
  - https://stackoverflow.com/questions/1546226/regex-to-validate-word-with-apostrophes-hyphens

- **Unicode-friendly word matching**
  - https://stackoverflow.com/questions/8465335/regex-word-character-with-unicode

- **Using collections.Counter for frequencies**
  - https://stackoverflow.com/questions/21312345/counting-frequency-of-words-in-a-list

- **Safe splitting using re.split**
  - https://stackoverflow.com/questions/4622393/split-string-based-on-operators-using-regex

### Python Documentation

- **re.findall —**
  - https://docs.python.org/3/library/re.html#re.findall

- **re.split —**
  - https://docs.python.org/3/library/re.html#re.split

- **collections.Counter —**
  - https://docs.python.org/3/library/collections.html#collections.Counter

## 2. Thought Process (Why I Designed the Code This Way)

I needed a text analyzer that:

- Counts total words
- Computes average word length
- Extracts longest words (all ties)
- Computes frequency (case-insensitive)
- Handles punctuation
- Supports apostrophes, hyphens, and Unicode words

I intentionally avoided simplistic approaches like `text.split()` because:

- It breaks on punctuation
- It cannot correctly handle cases like:
  - "foo-bar"
  - "café's"
  - "foo''bar"
  - Unicode words

Therefore, I used regular expressions, because regex solves these issues reliably and is the industry-standard tool for parsing words.

### Key design choices:

1. **Handling apostrophes**

   If there are multiple consecutive `'` characters (e.g., `foo''bar`), they create invalid tokens.
   I replaced sequences of multiple `'` with a single space:

   ```python
   text = re.sub(r"'{2,}", " ", text)
   ```

2. **Splitting on commas and colons**

   The instructions required handling punctuation, so I split large text blocks:

   ```python
   parts = re.split(r"[:,]", text)
   ```

3. **Regex Pattern Choice**

   I used:

   ```python
   pattern = r"\b\w+(?:['-]\w+)*\b"
   ```

   This matches:
   - Simple words → "hello"
   - Hyphenated → "foo-bar"
   - Apostrophes → "café's"
   - Unicode → "café", "naïve", "über"

4. **Frequency Calculation**

   `Counter` is the cleanest and fastest way:

   ```python
   frequency = Counter(w.lower() for w in words)
   ```

5. **Longest Words**

   I used a first-pass to find max length, second pass to collect unique longest words.

6. **Exception Handling**

   I added:
   - Type checking
   - Catching unexpected exceptions

   This allows the function to fail safely.

## 3. Alternatives Considered and Comparison

I evaluated three approaches:

### A. Manual Character-by-Character Tokenizer

**Pros:**
- Full control
- No regex dependency

**Cons:**
- Very long to write
- Harder to maintain
- Easily introduces bugs
- Poor readability

**Why rejected:**
Unnecessary complexity.

### B. str.split() + manual punctuation stripping

**Pros:**
- Very short code
- Beginner-friendly

**Cons:**
- Breaks on punctuation
- Treats "foo-bar" incorrectly
- Fails for Unicode
- Creates empty tokens

**Why rejected:**
Incorrect word extraction.

### C. Regex-based tokenizer (Chosen)

**Pros:**
- Clean
- Flexible
- Works for Unicode
- Handles hyphens and apostrophes
- Most reliable for real text

**Cons:**
- Requires writing a good regex

**Why chosen:**
Best balance of clarity, correctness, and maintainability.

## 4. Step-by-Step Development Notes (How I Built It)

### Step 1 — Type checking

Protect against non-string inputs.

```python
if not isinstance(text, str):
    raise TypeError("Input must be a string.")
```

### Step 2 — Preprocessing

Normalize invalid apostrophes:

```python
text = re.sub(r"'{2,}", " ", text)
```

### Step 3 — Split large chunks

Handle comma/colon-separated phrases:

```python
parts = re.split(r"[:,]", text)
```

### Step 4 — Extract valid words

Pattern:

```python
\b\w+(?:['-]\w+)*\b
```

Captured:
- café
- café's
- foo-bar
- foo'bar

### Step 5 — Compute metrics

**Word count**

```python
word_count = len(words)
```

**Average length**

```python
avg_length = round(sum(len(w) for w in words) / word_count, 2)
```

**Frequency**

```python
frequency = Counter(w.lower() for w in words)
```

**Longest words**

- First find `max_len`
- Then collect all unique longest words

### Step 6 — Add error handling

Catches:
- Wrong input types
- Unexpected internal errors

## 5. Problems Faced (New Section)

### Problem 1 — Apostrophes breaking words

Examples like:

café''s

foo''bar

produce invalid tokens.

Regex alone treats these as broken words.

**Fix:** Replace multiple apostrophes with a space.

### Problem 2 — Hyphenated words splitting incorrectly

Default `.split()` turns:

state-of-the-art

into:

state, of, the, art — which is wrong.

**Fix:** Custom regex to keep valid hyphenated words intact.

### Problem 3 — Unicode characters not detected

Characters like:

naïve, über, café

are ignored by simple `\w` on some regex engines.

**Fix:** Use Python's Unicode-aware `\w` + extended pattern structure.

### Problem 4 — Commas and colons creating empty tokens

A naive split creates:

`["hello", "", "world"]`

which pollutes counts.

**Fix:** `re.split` and post-filtering cleanly remove empty chunks.

## 6. Why This Solution Is Best

- ✔ Accurate word extraction
- ✔ Supports Unicode (café, über)
- ✔ Handles hyphens & apostrophes (foo-bar, "café's")
- ✔ Correct handling of malformed input
- ✔ Frequency handled cleanly with `Counter`
- ✔ Regex chosen prevents tokenization bugs
- ✔ Easily readable and maintainable
- ✔ Error handling included
- ✔ Matches expected output format
- ✔ More robust than simple split-based approaches

This solution gives correct results for all realistic text scenarios and is the most maintainable for future updates.
