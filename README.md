Code Examples in Python
==========================


Example 1 - Weighted Die:
-------------------------

####Task definition:

Let’s implement model of six sided die with weights on the sides, 
so we don't have an even probability distribution, 
die is weighted by a list of weights passed in at construction time.  

####Testing conditions: 

After 100k iterations of throwing this die, 
the results should closely match the desired distribution, 
and this should be reproducible in the unit test example.  

since these are weights on a probability distribution, these should sum to one, 
and the incoming array should be of length 6. 
You should throw if either of these preconditions is false

source files: `six_sided_dice.py` `six_sided_dice_numpy.py` test_weighted_dice

*** 

####Runtime example: 

	python 
	Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
	[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from six_sided_dice import SixSidedWeightedDie
	>>> weights = [.05, .10, .15, .2, .2, .3]
	>>> SixSidedWeightedDie(weights).throw_die()
	3

####run unittest:  

	`python -m unittest test_weighted_dice`


***

Example 2 - palindrome generator
--------------------------------

####Task definition:  

1.  Let's implement palindrome generator, which reads a string of chars as an input, 
	and produces unique palindromes (strings which read the same reversed) 
	unique means that any following value was never produced before. 
 
2.  first produces all 1 letter palindromes, 
	then 2 letter ones, then ... 

For example: 
if given string is 'abc', then 'a', 'aa', 'aba', etc are all legal results 
(i.e., you can repeat the input chars just not the result).


source files: `palindrome.py`

***

####runtime example: 

	python 
	Python 2.7.10 (v2.7.10:15c95b7d81dc, May 23 2015, 09:33:12) 
	[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from palindrome import palindromes
	>>> palindromes('abc');
	['a', 'c', 'b', 'aa', 'cc', 'bb', 'aba', 'aca', 'aaa', 'cbc', 'bbb', 'bcb', 'bab', 'cac', 'ccc']


####run unittest:  

	`python -m unittest test_weighted_dice`

***
