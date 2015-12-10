"""
model for a six sided die  
with weights on the sides, 
so that we don't have an even probability distribution, 
but it is weighted by a list of weights passed in at construction time.

since these are weights on a probability distribution, these should sum to one, and the incoming array
should be of length 6. You should throw if either of these preconditions is false

After a large number of iterations of throwing this die, the results should closely match the desired
distribution.

"""

class SixSidedWeightedDie(object):
    """
    NOTE: since these are weights on a probability distribution, these should sum to one, and the incoming array
    should be of length 6. You should throw if either of these preconditions is false
    """
    def __init__(self, weights):
        super(SixSidedWeightedDie, self).__init__()
        SIDES = 6 
        if len(weights) != SIDES: 
            raise ValueError('Oops! length of weights is not six')            
        if sum(weights) != 1: 
            raise ValueError('Oops! Sum of all weights is not equal to one')            
        self.weights = weights

        try:
            from random import random
            from itertools import takewhile
        except ImportError:
            print "Failed to import dependencies"

        self.random = random
        self.takewhile = takewhile
        self.elements = range(1, SIDES+1)
  
    def accumulate(self, iterable):
        """    
            Method generates a cumulative sum of elements. 
            accumulate([.05, .10, .15, .2, .2, .3]) -> .05 .15 .3 .5 .7 1
        """
        res = 0
        for _ in iterable:
            res += _
            yield res
    def throw_die(self):
        """
            Throw the die: this should produce a value in [1,6]
        """
        limit = self.random()
        return self.elements[sum(self.takewhile(bool, (value < limit for value in self.accumulate(self.weights))))]

