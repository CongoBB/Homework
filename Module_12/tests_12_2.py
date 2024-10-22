import unittest
from pprint import pprint

import runner_and_tournament


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.test_runner_1 = runner_and_tournament.Runner('test_runner_1', 10)
        self.test_runner_2 = runner_and_tournament.Runner('test_runner_2', 9)
        self.test_runner_3 = runner_and_tournament.Runner('test_runner_3', 3)

    def test_tournament_1(self):
        TournamentTest.all_results = runner_and_tournament.Tournament(90, self.test_runner_1,
                                                                      self.test_runner_3).start()
        self.assertTrue(self.all_results[2] is self.test_runner_3.name)
        return self.all_results

    def test_tournament_2(self):
        TournamentTest.all_results = runner_and_tournament.Tournament(90, self.test_runner_2,
                                                                      self.test_runner_3).start()
        self.assertTrue(self.all_results[2] is self.test_runner_3.name)
        return self.all_results

    def test_tournament_3(self):
        TournamentTest.all_results = runner_and_tournament.Tournament(90, self.test_runner_1,
                                                                      self.test_runner_2, self.test_runner_3).start()
        self.assertTrue(self.all_results[3] is self.test_runner_3.name)
        return self.all_results

    ## в runner_and_tournament добавил .name в строчку "finishers[place] = participant"

    @classmethod
    def tearDown(cls):
        print(cls.all_results)
