# Eaglepoint AI Technical Assessment

This repository contains the solutions for the Eaglepoint AI technical assessment, broken down into three distinct tasks. Each task demonstrates a specific set of skills ranging from text processing in Python to asynchronous JavaScript handling and rate limiting algorithms.

## Repository Structure

```
EAGLEPOINT-AI/
├── Task_1/                 # Smart Text Analyzer (Python)
│   ├── doc.md              # Detailed documentation and thought process
│   └── text_analyzer.py    # Source code
├── Task_2/                 # Async Data Fetcher (JavaScript)
│   ├── doc.md              # Detailed documentation and thought process
│   └── async_fetcher.js    # Source code
├── Task_3/                 # Rate Limiter (JavaScript)
│   ├── doc.md              # Detailed documentation and thought process
│   └── rate_limit.js       # Source code
└── README.md               # Project overview (this file)
```

## Tasks Overview

### Task 1: Smart Text Analyzer (Python)
A Python utility for analyzing text to extract meaningful statistics.
- **Features**: Word count, average length, frequency analysis, and extraction of longest words.
- **Highlights**: Robust regex handling for apostrophes, hyphens, and Unicode characters (e.g., "café", "foo-bar").
- **Usage**: `python Task_1/text_analyzer.py`

### Task 2: Async Data Fetcher (JavaScript)
A JavaScript module demonstrating robust asynchronous patterns.
- **Features**: Mock API simulation, retry logic with exponential backoff (or fixed delay), and error handling.
- **Highlights**: Uses `async/await` for clean, readable asynchronous control flow without callback hell.
- **Usage**: `node Task_2/async_fetcher.js`

### Task 3: Rate Limiter (JavaScript)
A custom implementation of a rate limiting mechanism.
- **Features**: Enforces a limit of 5 requests per user within a 60-second window.
- **Highlights**: Implements the **Fixed Window Counter** algorithm using a `Map` for O(1) performance and automatic resets.
- **Usage**: `node Task_3/rate_limit.js`

## Documentation
Each task folder contains a `doc.md` file with:
- **Search History**: References and resources used during development.
- **Thought Process**: Explanation of design choices and algorithm selection.
- **Alternatives Considered**: Why specific approaches were chosen over others.
- **Problems & Solutions**: Challenges faced during implementation and how they were resolved.

## How to Run
Ensure you have **Python 3.x** and **Node.js** installed.

1. **Clone the repository:**
   ```bash
   git clone <https://github.com/Dawit212119/EAGLEPOINT-AI.git>
   cd EAGLEPOINT-AI
   ```

2. **Run Task 1 (Python):**
   ```bash
   python Task_1/text_analyzer.py
   ```

3. **Run Task 2 (JavaScript):**
   ```bash
   node Task_2/async_fetcher.js
   ```

4. **Run Task 3 (JavaScript):**
   ```bash
   node Task_3/rate_limit.js
   ```

