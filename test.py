'''
Created on 24 мар. 2020 г.

@author: maxx
'''
import unittest
import Finder
import time
import itertools
import string


class Test(unittest.TestCase):

    def testWrongInitParams(self):
        with self.assertRaises(TypeError):
            Finder.Finder('')
        with self.assertRaises(TypeError):
            Finder.Finder([1, '2'])
        self.assertIsInstance(Finder.Finder([]), Finder.Finder)
        self.assertIsInstance(Finder.Finder(['1', '2']), Finder.Finder)
        
    def testSimpleCases(self):
        f = Finder.Finder(['abc', 'aabcd'])
        self.assertSetEqual(set(['abc']), set(f.find('abc')))
        self.assertSetEqual(set(['aabcd']), set(f.find('cbada')))
        self.assertListEqual([], f.find('cbade'))
        f = Finder.Finder(['abc', 'aabcd', 'adcba'])
        self.assertSetEqual(set(['aabcd', 'adcba']), set(f.find('dbcaa')))

    def testBigInitialisationWith100K(self):
        cur_initialisation = []
        max_count = 100000
        for val in itertools.permutations(string.ascii_lowercase):
            max_count -= 1
            if max_count <= 0:
                break
            cur_initialisation.append("".join(val))
            
        startTime = time.time_ns() / (10 ** 9)
        testFinder = Finder.Finder(cur_initialisation)
        print('%s init: %.6f sec' % (self.id(), time.time_ns() / (10 ** 9) - startTime))
        
        startTime = time.time_ns() / (10 ** 9)
        res = testFinder.find("".join(string.ascii_lowercase))
        print('%s find: %.6f sec' % (self.id(), time.time_ns() / (10 ** 9) - startTime))
        self.assertSetEqual(set(res), set(cur_initialisation))
        
    def testBigInitialisationWith2KAndFind50kTimes(self):
        init_lower_case = []
        init_all = []
        max_count = 1000
        for val in itertools.permutations(string.ascii_lowercase):
            max_count -= 1
            if max_count <= 0:
                break
            init_lower_case.append("".join(val))
            init_all.append("".join(val))
            
        max_count = 1000
        for val in itertools.permutations(string.ascii_uppercase):
            max_count -= 1
            if max_count <= 0:
                break
            init_all.append("".join(val))            
            
        startTime = time.time_ns() / (10 ** 9)
        testFinder = Finder.Finder(init_all)
        print('%s init: %.6f sec' % (self.id(), time.time_ns() / (10 ** 9) - startTime))
        
        startTime = time.time_ns() / (10 ** 9)
        for _ in range(50000):
            res = testFinder.find("".join(string.ascii_lowercase))
        print('%s 50K Find: %.6f sec' % (self.id(), time.time_ns() / (10 ** 9) - startTime))
        self.assertSetEqual(set(res), set(init_lower_case))

        
if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testWrong']
    unittest.main()
