"""
model for a six sided die  
with weights on the sides, 
so that we don't have an even probability distribution, 
but it is weighted by a list of weights passed in at construction time.

since these are weights on a probability distribution, these should sum to one, and the incoming array
should be of length 6. You should throw if either of these preconditions is false

After a large number of iterations of throwing this die, the results should closely match the desired
distribution.

using numpy.random library 
"""

class SixSidedWeightedDie(object):
    def __init__(self, weights):
        super(SixSidedWeightedDie, self).__init__()
        if sum(weights) != 1: 
            raise ValueError('Oops! Sum of all weights is not equal to one')        
        if len(weights) != 6: 
            raise ValueError('Oops! length of weights is not six')
        self.weights = weights
        self.elements = range(1,7)
        try:
            from numpy.random import choice
        except ImportError:
            print "Unable to import numpy module as a dependency"
        self.choice = choice
    # Throw the die: this should produce a value in [1,6]
    def throw_die(self):
        return self.choice(self.elements, p=self.weights)
