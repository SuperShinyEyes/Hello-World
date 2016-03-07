from time import time

def speak(topic):
    print "My speach is " + topic

def timer(fn):
    def inner(*args, **kwargs):
        t = time()
        fn(*args, **kwargs)
        print "took {time}".format(time=time()-t)

    return inner

speaker = timer(speak)
speaker("FP with Python")


def log(level, message):
    print "[{level}]: {msg}".format(level=level, msg=message)

from functools import partial
debug = partial(log, "debug")

debug("Start doing something")
debug("Continue with something else")
debug("Finished. Profit?")


from functools import partial
basetwo = partial(int, base=2)
basetwo.__doc__ = 'Convert base 2 string to an int.'
print(basetwo('10010'))



def fsum(f):
    def frame():
        # return sum([f(i) for i in range(1,11)])
        return sum(map(f, range(1,11)))
    return frame

log_sum = fsum(math.log)
log_sum()
