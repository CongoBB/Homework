import unittest
import runner
import runner_and_tournament
import rt_with_exceptions


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        """
        Test for walk function
        """
        test_runner = runner.Runner('test_runner')
        for i in range(10):
            runner.Runner.walk(test_runner)
        self.assertEqual(test_runner.distance, 50)

    def test_run(self):
        """
        Test for run function
        """
        test_runner = runner.Runner('test_runner')
        for i in range(10):
            runner.Runner.run(test_runner)
        self.assertEqual(test_runner.distance, 100)

    def test_challenge(self):
        test_runner_1 = runner.Runner('test_runner_1')
        test_runner_2 = runner.Runner('test_runner_2')
        for i in range(10):
            runner.Runner.run(test_runner_1)
            runner.Runner.walk(test_runner_2)
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)
