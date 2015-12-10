"""
1.  Let's implement palindrome generator, which reads a string of chars as an input, 
    and produces unique palindromes (strings which read the same reversed) 
    unique means that any following value was never produced before. 
 
2.  first produces all 1 letter palindromes, 
    then 2 letter ones, then ... 

For example: 
if given string is 'abc', then 'a', 'aa', 'aba', etc are all legal results 
(i.e., you can repeat the input chars just not the result).

"""
import unittest
import itertools

def palindromes(seed):
    try:
        seed=str(seed)
    except ValueError: 
        print "Failed to read input args"
    if len(seed) > 8: 
        raise ValueError('String is too long, Ill hang :-)')        
    def ispalindrome(someword): return someword == someword[::-1]
    res = [] 
    for i in xrange(1, len(seed)+1):
        res += list(set(filter(ispalindrome, [''.join(_) for _ in itertools.product(seed, repeat=i)])))
    return res   

class TestPalindromes(unittest.TestCase):
    def test_palindromes(self):
        NUM_PROBES = 4000
        for seed in ['abc', 'a', 'elephant']:
            responses = set()
            for _, response in itertools.izip(xrange(NUM_PROBES), palindromes(seed)):
                self.assertNotIn(response, responses)
                for i in xrange(-(-len(response)//2)):
                    self.assertEqual(response[i], response[-(i+1)]) 
                responses.add(response)
