

async function mockAPi(url) {

    return new Promise((resolve, reject) => {
        const success = Math.random() > 0.5;

        setTimeout(() => {
            if (success) {
                resolve({ data: `Fetched data from ${url}` })
            }
            else {
                reject(new Error(`Failed to fetch data from ${url}`))
            }
        }, 300)
    })
}

function wait(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

async function fetchDataWithRetry(url, maxRetires = 3) {

    let attempt = 0;
    while (attempt <= maxRetires) {
        try {
            const response = await mockAPi(url);
            return response;
        } catch (error) {
            attempt++;
            console.warn(`Attempt ${attempt} failed: ${error.message}`);
            if (attempt > maxRetires) {
                throw new Error(`All ${maxRetires} attempts failed for ${url}`);
            }
            await wait(500); // wait before retrying

        }
    }
}

(async () => {
    const url = "https://example.com/api/data";
    try {
        const result = await fetchDataWithRetry(url, 3);
        console.log("Data fetched successfully:", result);
    } catch (error) {
        console.error("Final error after retries:", error.message);
    }
})();