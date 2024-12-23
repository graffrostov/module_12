import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        test_walk_value = runner.Runner('test_walk_value')
        for i in range(10):
            test_walk_value.walk()
        self.assertEqual(test_walk_value.distance,50)


    def test_run(self):
        test_run_value = runner.Runner('test_run_value')
        for i in range(10):
            test_run_value.run()
        self.assertEqual(test_run_value.distance, 100)


    def test_challenge(self):
        test_walk_value = runner.Runner('test_walk_value')
        test_run_value = runner.Runner('test_run_value')
        for i in range(10):
            test_walk_value.walk()
            test_run_value.run()
        self.assertNotEqual(test_walk_value.distance, test_run_value.distance)



if __name__ == '__main__':
    unittest.main()

#
# def test_walk(self):
#     test_walk_value = runner.Runner('test_walk_value')
#     for i in range(10):
#         test_walk_value.walk()
#     self.assertEqual(test_walk_value.distance,450)

# Ran 3 tests in 0.015s
#
# FAILED (failures=1)
#
#
# 450 != 50
#
# Expected :50
# Actual   :450
# <Click to see difference>
#
# Traceback (most recent call last):
#   File "D:\Univer\module_12\tests_12_1.py", line 11, in test_walk
#     self.assertEqual(test_walk_value.distance,450)
# AssertionError: 50 != 450
#
#
# Process finished with exit code 1