def collect_data(file_name):
    def decorator(func):
        def worker(*args, **kwargs):
            res = func(*args, **kwargs)
            with open(file_name, "a") as log_file:
                log_file.write(str(res) + "\n")
            return res
        return worker
    return decorator

