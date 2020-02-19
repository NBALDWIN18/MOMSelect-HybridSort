from random import randint
from MedianOMedians import median_of_medians
from HybridSort import HybridSort
import unittest

'''
Generates a random list of ints
:param size: the size of the list
:param range: a list of size 2, with the low and high bounds
:return: a list of random ints
'''
def RandomList(size, bounds=[0,100]):
    rl = []
    for i in range(size):
        rl.append(randint(*bounds))
    return rl

class HomeWork02_Test(unittest.TestCase):

    '''
    Tests Mom Select
    '''
    def test_Mom(self):
        passes = 0
        fails = 0
        print("Testing MOM Select ...")
        for i in range(10):
            rl = RandomList(1000)
            rl_sorted = sorted(rl)
            k = [3,4,5,6,7,8,9,10]
            for j in range (1,len(rl)):
                try:
                    a = rl_sorted[j-1]
                    b = median_of_medians(rl,j,k[j%len(k)])
                    self.assertEqual(a,b)
                    passes += 1
                except AssertionError:
                    fails += 1
        print("Passes",passes,"\nFails",fails)

    '''
    Test Hybrid Sort
    '''
    def test_Hybrid(self):
        passes = 0
        fails = 0
        print("Testing Hybrid Sort ...")
        for i in range(1000):
            rl = RandomList(1000)
            rl_sorted = sorted(rl)

            config = RandomList((i%6)+1, [1,2])
            rl = HybridSort(rl,config)
            try:
                self.assertEqual(rl_sorted,rl)
                passes += 1
            except AssertionError:
                fails+=1
        print("Passes",passes,"\nFails",fails)

'''
Main Functions
:return: None
'''
'''
def main():
    Test = HomeWork02_Test()
    Test.Test_Mom()
    print()
    Test.Test_Hybrid()
'''
if __name__ == '__main__':
    unittest.main()
