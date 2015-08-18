from datetime import datetime
from functools import wraps

def timed(func):
  ''' Benchmarking wrapper '''
  @wraps(func)
  def decorated(*args, **kwargs):
    pre_t = datetime.utcnow()
    result = func(*args, **kwargs)
    post_t = datetime.utcnow()
    duration = (post_t - pre_t).total_seconds()
    print "\t%s: %.2f sec" % (func, duration)
    return result
  return decorated

@timed
def main():
  result=1
  y=100000
  while y>0:
    result*=y
    y-=1
  print type(result)

main()
