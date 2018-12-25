from time import time
def pre(data):
    print(data+', hello')
    return 
def benchmarking(token, preprocess_fn, *pre_args, **pre_kwargs):
    def decorator(inference_fn):
        def wrapper(*args,**kwargs):
            if preprocess_fn is not None:
                preprocess_fn(*pre_args, **pre_kwargs)
            s = time()
            metric = inference_fn(*args, **kwargs)
            e = time()
            inference_time = e - s
            print("metric:{}, {} s".format(metric, inference_time))
            return metric, inference_time
        return wrapper
    return decorator
'''
@benchmarking(token='0xcd', preprocess_fn=pre)
def foo():
    print('world')
    return 666
'''
