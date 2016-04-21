# l1 = [1,2,3,4,5, 0]
# l2 = [-1,2,0,3,4,-5]
l1 =[2424, 5114, 3769, 2962, 8342, 541, 6279, 8342, 3500, 8611, 5114, 6459]
l2 =[12559, 7269, 6193, 4579, 6462, 3503, 5386, 7807, 1620, 275, 6193, 4848]

l1.sort()
l2.sort()
l2.reverse()
print(l1, l2)
def pairSum(l1, l2, t):
    for i in l1:
        for j in l2:
            s = i + j
            if s == t:
                return i, j
            elif s < t:
                break

    return None

print(pairSum(l1, l2, 18838))


def fact(n):
    def iterate(i, acc):
        if(i > n): return acc
        else: return iterate(i+1, acc*i)
    return iterate(2, 1)


def tail_call_optimized(g):
    def func(*args, **kwargs):
        f = sys._getframe()
        if f.f_back and f.f_back.f_back and f.f_back.f_back.f_code == f.f_code:
            raise TailRecurseException(args, kwargs)
    else:
    while 1:
    try:
    return g(*args, **kwargs)
    except TailRecurseException, e:
    args = e.args
    kwargs = e.kwargs
    func.__doc__ = g.__doc__
    return func
