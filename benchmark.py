from time import time
def benchmarking(preprocess_fn):
    def decorator(inference_fn):
        def wrapper(model, data_loader):
            if preprocess_fn is not None:
                preprocess_fn()
            s = time()
            metric = inference_fn(model, data_loader)
            e = time()
            inference_time = e - s
            return metric, inference_time
        return wrapper
    return decorator
