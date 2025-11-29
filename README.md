# Eaglepoint AI Technical Assessment

This repository contains the solutions for the Eaglepoint AI technical assessment. The project is divided into three tasks, each containing its own source code and detailed documentation of the development process.

## Repository Structure

```
EAGLEPOINT-AI/
├── Task_1/
│   ├── doc.md              # Documentation: Steps, Searches, Thought Process
│   └── text_analyzer.py    # Task 1 Source Code
├── Task_2/
│   ├── doc.md              # Documentation: Steps, Searches, Thought Process
│   └── async_fetcher.js    # Task 2 Source Code
├── Task_3/
│   ├── doc.md              # Documentation: Steps, Searches, Thought Process
│   └── rate_limit.js       # Task 3 Source Code
└── README.md               # Project Overview & Summary
```

## Documentation of Steps & Thought Process

Per the submission requirements, the detailed steps followed, searches made, and problems solved are documented in the `doc.md` files located within each task's directory.

- **[Task 1 Documentation (Python Text Analyzer)](Task_1/doc.md)**
  - Covers regex strategy for handling apostrophes and Unicode.
  - Explains the choice of `collections.Counter`.
  - Lists specific Google searches and StackOverflow references.

- **[Task 2 Documentation (Async Fetcher)](Task_2/doc.md)**
  - Details the implementation of the retry logic and mock API.
  - Explains the decision to use `async/await` over Promise chains.
  - Documents the search terms used for async patterns.

- **[Task 3 Documentation (Rate Limiter)](Task_3/doc.md)**
  - Explains the "Fixed Window Counter" algorithm choice.
  - Documents the trade-offs between using a `Map` vs. Redis.
  - Steps taken to ensure O(1) performance.

## Tasks Overview

### Task 1: Smart Text Analyzer (Python)
A Python utility for analyzing text to extract meaningful statistics.
- **Features**: Word count, average length, frequency analysis, and extraction of longest words.
- **Highlights**: Robust regex handling for apostrophes, hyphens, and Unicode characters.

### Task 2: Async Data Fetcher (JavaScript)
A JavaScript module demonstrating robust asynchronous patterns.
- **Features**: Mock API simulation, retry logic with 1-second delay, and error handling.
- **Highlights**: Uses `async/await` for clean control flow.

### Task 3: Rate Limiter (JavaScript)
A custom implementation of a rate limiting mechanism.
- **Features**: Enforces a limit of 5 requests per user within a 60-second window.
- **Highlights**: Efficient O(1) implementation using JavaScript `Map`.

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
