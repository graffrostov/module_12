import unittest
import  test_12_3


test_unit = unittest.TestSuite()

test_unit.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.RunnerTest))
test_unit.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))



runner = unittest.TextTestRunner(verbosity=2)
runner.run(test_unit)