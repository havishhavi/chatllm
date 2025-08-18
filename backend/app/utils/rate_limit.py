from fastapi import Request, HTTPException
from time import time
from collections import defaultdict

# Allow max 5 requests per 60 seconds
RATE_LIMIT = 5
WINDOW_SECONDS = 60

request_log = defaultdict(list)

def check_rate_limit(identifier: str):
    now = time()
    window = request_log[identifier]

    # Keep only recent timestamps
    window[:] = [ts for ts in window if now - ts < WINDOW_SECONDS]


    if len(window) >= RATE_LIMIT:
        raise HTTPException(status_code=429, detail="Rate limit exceeded.")

    window.append(now)
