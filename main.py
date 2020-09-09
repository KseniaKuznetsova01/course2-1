import functools
import json

def decorator(func):
  @functools.wraps(func)
  def wrapped(*args, **kwargs):
    x = func(*args, **kwargs)
    result = json.dumps(x)
    return result
  return wrapped



@decorator
def change(*args):
  return args

print (change({"name": "Ksenia", "age":  19}))