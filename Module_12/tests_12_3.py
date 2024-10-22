import unittest

import runner_and_tournament


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_walk(self):
        test_runner = runner_and_tournament.Runner('test_runner')
        for i in range(10):
            runner_and_tournament.Runner.walk(test_runner)
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_run(self):
        test_runner = runner_and_tournament.Runner('test_runner')
        for i in range(10):
            runner_and_tournament.Runner.run(test_runner)
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_challenge(self):
        test_runner_1 = runner_and_tournament.Runner('test_runner_1')
        test_runner_2 = runner_and_tournament.Runner('test_runner_2')
        for i in range(10):
            runner_and_tournament.Runner.run(test_runner_1)
            runner_and_tournament.Runner.walk(test_runner_2)
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


class TournamentTest(unittest.TestCase):
    all_results = {}
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def setUp(self):
        self.test_runner_1 = runner_and_tournament.Runner('test_runner_1', 10)
        self.test_runner_2 = runner_and_tournament.Runner('test_runner_2', 9)
        self.test_runner_3 = runner_and_tournament.Runner('test_runner_3', 3)

    @unittest.skipIf(is_frozen, 'Tests in this test case are frozen')
    def test_tournament_1(self):
        TournamentTest.all_results = runner_and_tournament.Tournament(90, self.test_runner_1,
                                                                      self.test_runner_3).start()
        self.assertTrue(self.all_results[2] is self.test_runner_3.name)
        return self.all_results

    @unittest.skipIf(is_frozen, 'Tests in this test case are frozen')
    def test_tournament_2(self):
        TournamentTest.all_results = runner_and_tournament.Tournament(90, self.test_runner_2,
                                                                      self.test_runner_3).start()
        self.assertTrue(self.all_results[2] is self.test_runner_3.name)
        return self.all_results

    @unittest.skipIf(is_frozen, 'Tests in this test case are frozen')
    def test_tournament_3(self):
        TournamentTest.all_results = runner_and_tournament.Tournament(90, self.test_runner_1,
                                                                      self.test_runner_2, self.test_runner_3).start()
        self.assertTrue(self.all_results[3] is self.test_runner_3.name)
        return self.all_results

    @classmethod
    def tearDownClass(cls):
        pass
