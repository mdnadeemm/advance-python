class RateLimiter:
    def __init__(self, limit):
        self.limit = limit

    def __call__(self):
        if self.limit > 0:
            self.limit -= 1
            return "Allowed"
        else:
            return "Blocked"


limiter = RateLimiter(3)


print(limiter())
print(limiter())
print(limiter())
print(limiter())
