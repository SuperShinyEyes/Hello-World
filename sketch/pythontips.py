def add_to(element, target=None):
    target = [] if target is None else target
    target.append(element)
    print target


add_to(1)
# Output: [1]

add_to(2)
# Output: [1, 2]

add_to(3)

add_to(3, [1])
