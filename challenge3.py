def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    func(*args, **kwargs)
                except Exception:
                    print(f"Attempt {attempt + 1} failed")

        return wrapper

    return decorator


@retry(3)
def download():
    print("...")


download()
