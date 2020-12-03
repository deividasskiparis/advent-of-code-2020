import time


def timed(name: str):
    def inner(f):
        def inner2(*args, **kwargs):
            start_time = time.time()
            r = f(*args, **kwargs)
            end_time = time.time()
            print("-" * 20 + f" {name} took {(end_time - start_time):.3f}s to complete " + "-" * 20)
            print()
            return r
        
        return inner2
    
    return inner
