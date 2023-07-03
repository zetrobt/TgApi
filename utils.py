from functools import wraps
from inspect import getmembers, getargspec, ismethod
from requests import Session
from requests.compat import urljoin

def _base_url(func, base):
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        argname = 'url'
        argspec = getargspec(func)

        if argname in kwargs:
            kwargs[argname] = urljoin(base, kwargs[argname])
        else:
            for i, name in enumerate(argspec[0]):
                if name == argname:
                    args = list(args)
                    args[i-1] = urljoin(base, args[i-1])
                    break

        return func(*args, **kwargs)
    return wrapper

def inject_base_url(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        argname = 'base_url'

        if argname in kwargs:
            obj = args[0]
            
            for name, method in getmembers(obj, ismethod):
                argspec = getargspec(method.__func__)

                if 'url' in argspec[0]:
                    setattr(obj, name, _base_url(method, kwargs[argname]))

            del kwargs[argname]

        return func(*args, **kwargs)
    return wrapper
    
setattr(
    Session,
    '__init__',
    inject_base_url(getattr(Session, '__init__'))
  
