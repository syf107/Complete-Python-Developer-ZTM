import unittest
import script

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = script.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shawdasjhd'
        result = script.do_stuff(test_param)
        self.assertIsInstance(result, TypeError)

    def test_do_stuff3(self):
        test_param = None
        result = script.do_stuff(test_param)
        self.assertEquals(result, 'please enter number')
    
    def test_do_stuff4(self):
        test_param = ''
        result = script.do_stuff(test_param)
        self.assertEquals(result, 'please enter number')

if __name__ == '__main__':
    unittest.main()