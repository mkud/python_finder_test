# Test task `Finder`

Short task description:
* create class `Finder`;
* this class is initialized with a list of strings;
* the class contains a method `find`, which return all strings from the init list that contain the exact same characters as the string passed into this method.

[Here is the full task](TASK.md)

# Result

* `Finder.py` - class implementation;
* `test.py` - unit-tests.

# How to use class `Finder`

	import Finder
	
	f = Finder.Finder(['ab', 'abc'])
	result = f.find('ab')

# How to run tests

	$ python3 test.py 
	
	__main__.Test.testBigInitialisationWith100K init: 0.854741 sec
	__main__.Test.testBigInitialisationWith100K find: 0.075356 sec
	__main__.Test.testBigInitialisationWith2KAndFind50kTimes init: 0.017694 sec
	__main__.Test.testBigInitialisationWith2KAndFind50kTimes 50K Find: 21.066653 sec
	
	----------------------------------------------------------------------
	Ran 4 tests in 22.095s
	
	OK
