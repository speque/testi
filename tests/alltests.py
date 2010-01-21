import unittest
import test_investigator
import test_location
import test_area
import test_board
import test_skillcheck

if __name__=="__main__":
	print ''
	print '******************************************'
	print '* Test suite for Turku Horror initiated: *'
	print '******************************************'
	print ''
	investigatorSuite = test_investigator.suite()
	locationSuite = test_location.suite()
	areaSuite = test_area.suite()
	boardSuite = test_board.suite()
	skillcheckSuite = test_skillcheck.suite()
	allTestSuites = unittest.TestSuite([investigatorSuite, locationSuite, areaSuite, \
	boardSuite, skillcheckSuite])
	runner = unittest.TextTestRunner(verbosity=2)
	runner.run(allTestSuites)
