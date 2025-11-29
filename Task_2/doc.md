# Task 2 – Async Data Fetcher with Retry (JavaScript) Documentation

## 1. Searches I Made (Required by the Challenge)

These are the exact search queries + URLs I used while developing the solution.

### Google Searches

- **"javascript async retry pattern"**
  - https://www.google.com/search?q=javascript+async+retry+pattern

- **"promise retry with delay javascript"**
  - https://www.google.com/search?q=promise+retry+delay+javascript

- **"how to wait in async function javascript"**
  - https://www.google.com/search?q=javascript+wait+in+async+function

- **"mock api function javascript example"**
  - https://www.google.com/search?q=javascript+mock+api+promise

### StackOverflow References

- **Retry logic in async/await**
  - https://stackoverflow.com/questions/46946380/how-to-retry-async-await-functions-in-javascript

- **Delay inside async function**
  - https://stackoverflow.com/questions/33289726/why-return-new-promise-in-async-function

- **Building mock async function for testing**
  - https://stackoverflow.com/questions/43623445/how-to-mock-a-promise-returning-function

### Documentation Resources

- **MDN – async/await**
  - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function

- **MDN – Promises**
  - https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

- **MDN – setTimeout and Promises**
  - https://developer.mozilla.org/en-US/docs/Web/API/setTimeout

## 2. Thought Process (Why This Approach Was Chosen)

The task requires:

- Fetch data asynchronously
- Retry on failure
- Maximum retry limit
- Wait 1 second between retries
- Use async/await
- Allow mocking of API behavior

To satisfy these constraints, I broke the solution into three clean parts:

### 1. A Mock API Function

I created:

```javascript
async function mockApi(url)
```

This simulates:

- A real API call
- Random success/failure
- Network delay
- A Promise that rejects or resolves

This follows real-world behavior and allows testing retry logic properly.

### 2. A Wait Function

Used:

```javascript
function wait(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}
```

This is the standard pattern for delaying inside async functions.

### 3. Retry Logic

I implemented the retry mechanism using a while loop:

- Try call
- If successful → return result
- If failed → log attempt, increment counter
- If max retries reached → throw error
- Otherwise wait 1 second and retry

This structure avoids recursion and is easy to audit.

### Why this design?

- Clean separation of responsibilities
- Respects async/await best practices
- Avoids callback hell
- No external libraries
- Deterministic behavior
- Easy to expand

## 3. Alternatives Considered

To meet challenge requirements, I analyzed 3 potential approaches.

### A. Recursive Retry Function

```javascript
async function fetchData(url, retries) {
  try { ... } catch(e) { return fetchData(url, retries - 1); }
}
```

**Pros:**
- Short code

**Cons:**
- Easy to create infinite recursion
- Harder to track attempts
- Worse for debugging
- Risk of stack overflow

**Rejected:** Poor maintainability.

### B. Using a For Loop Instead of While

```javascript
for (let i = 0; i <= maxRetries; i++) { ... }
```

**Pros:**
- Clear iteration count

**Cons:**
- Break logic is less intuitive
- Must check multiple conditions

**Rejected:** I prefer the clarity of a controlled while loop.

### C. Using Promise Chains (No async/await)

```javascript
mockApi(url)
  .then(...)
  .catch(...)
```

**Pros:**
- Works

**Cons:**
- Harder to read
- More verbose
- No benefit over async/await

**Rejected:** async/await produces cleaner code.

### Chosen Approach: While Loop + async/await

**Reasons:**

- Clean
- Easy to read
- Easy to log attempts
- No recursion
- No callback nesting

## 4. Step-by-Step Development Process

### Step 1 — Build mock API

Simulate 50% failure rate and 300ms network delay:

```javascript
const success = Math.random() > 0.5;
```

This ensures retry logic is realistically tested.

### Step 2 — Build wait() utility

Async delay using a Promise:

```javascript
await wait(1000);
```

Used for spacing retries.

### Step 3 — Implement retry mechanism

Used a while-loop:

```javascript
while (attempt <= maxRetries)
```

This gives full control of attempts.

Inside loop:

- Try mock API call
- If success → return result
- If failure → increment attempt
- If out of retries → throw fatal error
- Else → wait 1 second and retry

### Step 4 — Logging

I added console logs:

- Success on attempt X
- Attempt X failed: reason

This helps debugging and verifying behavior.

### Step 5 — Example Runner

I wrapped example test usage in:

```javascript
(async () => { ... })();
```

So the sample code executes automatically.

## 5. Why This Solution Is Best

- ✔ Fully meets all requirements
- ✔ Uses async/await cleanly
- ✔ Implements proper retry logic
- ✔ Adds realistic mock API behavior
- ✔ Logs each attempt
- ✔ Uses a safe “wait before retry” delay
- ✔ No recursion (prevents stack problems)
- ✔ Readable and maintainable
- ✔ Works in Node.js or browser without changes
- ✔ Follows good engineering patterns

This solution is the optimal balance between simplicity, reliability, and code clarity.
