import unittest
from AKDSFramework.structure import ArrayQueue

class Test(unittest.TestCase):
    def setUp(self):
        self.q = ArrayQueue(4)

    def test_queue_build(self):
        self.assertEqual('[]', str(self.q))
    
    def test_queue_enqueue(self):
        self.q.enqueue(12)
        self.assertEqual('[12]', str(self.q))
    
    def test_dequeue(self):
        self.q.enqueue(12)
        dqueue = self.q.dequeue()

        self.assertEqual(12, dqueue)

    def test_access(self):
        self.q.enqueue(12)
        self.q.enqueue(13)
        self.assertEqual(13, self.q[1])

    def test_iteration(self):
        self.q.enqueue(12)
        self.q.enqueue(13)
        testing_string = ''
        for data in self.q:
            testing_string += str(data) + ' '
        self.assertEqual('12 13 ', testing_string)

if __name__ == '__main__':
    print('Queue Tests Running')
    unittest.main()