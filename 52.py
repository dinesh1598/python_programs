#Reverse the tuple

tuples = (45, 54, 23, 12, 2, 9)
#method 1


def rev_tuple(numbers):
   return numbers[::-1]
print(rev_tuple(tuples))

#method 2
def reversed_tuple(parameter):
    rev = tuple(reversed(parameter))
    return rev
print(reversed_tuple(tuples))