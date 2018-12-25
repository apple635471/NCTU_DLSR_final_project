from time import time
def timing(preprocess_fn):
    def decorator(inference_fn):
        def wrapper(model, data_loader):
            if preprocess_fn is not None:
                preprocess_fn()
            s = time()
            inference_fn(model, data_loader)
            e = time() 
            return e - s
        return wrapper
    return decorator
