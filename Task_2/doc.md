# Async Fetcher Documentation

## Overview
The `async_fetcher.js` script demonstrates a robust asynchronous data fetching pattern using JavaScript Promises and `async/await`. It includes a mock API function and a utility to fetch data with automatic retries upon failure.

## Functions

### `mockAPi(url)`
Simulates an asynchronous network request.
- **Parameters**: `url` (string) - The URL to fetch from.
- **Returns**: A `Promise` that:
  - Resolves with `{ data: ... }` if successful (50% chance).
  - Rejects with an `Error` if failed.
- **Delay**: 300ms.

### `wait(ms)`
A utility function that creates a delay.
- **Parameters**: `ms` (number) - Milliseconds to wait.
- **Returns**: A `Promise` that resolves after the specified duration.

### `fetchDataWithRetry(url, maxRetires = 3)`
Attempts to fetch data from the given URL, retrying up to a specified number of times if the request fails.

- **Parameters**:
  - `url` (string): The target URL.
  - `maxRetires` (number): Maximum number of retry attempts (default: 3).
- **Returns**: A `Promise` that resolves with the API response if successful.
- **Throws**: An `Error` if all attempts fail.

### Logic Details
1. **Retry Loop**: A `while` loop controls the attempts, running as long as `attempt <= maxRetires`.
2. **Error Handling**: 
   - If `mockAPi` fails, the error is caught.
   - A warning is logged to the console (`console.warn`).
   - The current attempt counter is incremented.
3. **Backoff Strategy**: Uses a fixed delay of 500ms between retries using the `wait` function.
4. **Failure**: If the attempt count exceeds `maxRetires`, the function throws a final error indicating total failure.

### Example Usage

```javascript
(async () => {
    const url = "https://example.com/api/data";
    try {
        const result = await fetchDataWithRetry(url, 3);
        console.log("Data fetched successfully:", result);
    } catch (error) {
        console.error("Final error after retries:", error.message);
    }
})();
```

