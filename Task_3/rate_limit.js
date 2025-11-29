



class RateLimiter {
    constructor(limit = 5, windowMs = 60000) {
        this.limit = limit;
        this.windowMs = windowMs;

        this.users = new Map();
    }


    isAllowed(userId) {
        const now = Date.now();
        if (!this.users.has(userId)) {
            this.users.set(userId, {
                count: 1,
                firstRequestTime: now
            })
            return true;
        }
        const userData = this.users.get(userId);
        if (now - userData.firstRequestTime >= this.windowMs) {
            userData.count = 1;
            userData.firstRequestTime = now;
            return true;
        }

        if (userData.count < this.limit) {
            userData.count++;
            return true;
        }

        return false;
    }
}

const limiter = new RateLimiter(5, 60000)

function simulateRequest(userId) {
    const allowed = limiter.isAllowed(userId);
    const status = allowed ? "allowed" : "blocked";
    console.log(`User ${userId} request is ${status}`);
}


console.log("Simulating requests for User A:");
for (let i = 0; i <= 5; i++) {
    simulateRequest("UserA");
}

console.log("\nSimulating the 6th requests for User A:");
simulateRequest("UserA");
console.log("\nSimulating the 7th requests for User A:");

simulateRequest("UserA");
simulateRequest("UserA");

