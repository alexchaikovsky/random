import unittest
import rm

class TestRemoveDups(unittest.TestCase):

    def test_remove_dups_hashable(self):

        l1 = [1, 2, 3, 1]
        l2 = [1, 3, 2, 1, 5, 3, 5, 1, 4]
        l3 = [(1,2),(2,3),(1,2),(3,4)]
        l4 = ['abc','efg','cde','abc','cde']
        l5 = [1,3,1,2,'asd',(1,2), 'bce','asd',(0,1),(1,2),3,4]
        
        self.assertEqual(rm.remove_duplicates(l1), [1, 2, 3])
        self.assertEqual(rm.remove_duplicates(l2), [1, 3, 2, 5, 4])
        self.assertEqual(rm.remove_duplicates(l3), [(1, 2), (2, 3), (3, 4)])
        self.assertEqual(rm.remove_duplicates(l4), ['abc','efg','cde'])
        self.assertEqual(rm.remove_duplicates(l5), [1, 3, 2, 'asd', (1, 2), 'bce', (0, 1), 4])
    
    def test_remove_dups_unhashable(self):
        from collections import deque
        d1 = deque('ghi')
        d2 = deque('abc')
        d3 = deque('efg')
        d4 = deque('abc')
        
        t1 = [d1,d3,d1,d3,d2,d4]
        self.assertEqual(rm.remove_duplicates(l4), [d1,d3,d2])
        
        t2 = [[1,2], [4,5], [2,3], [1,2], [3,4], [2,3]]
        self.assertEqual(rm.remove_duplicates(l5), [[1, 2], [4, 5], [2, 3], [3, 4]])
        

if __name__ == '__main__':
    unittest.main()
    
