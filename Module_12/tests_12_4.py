import logging
import rt_with_exceptions
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_walk(self):
        try:
            test_runner = rt_with_exceptions.Runner('test_runner', -1)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)

        for i in range(10):
            rt_with_exceptions.Runner.walk(test_runner)
        self.assertEqual(test_runner.distance, 50)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_run(self):
        try:
            test_runner = rt_with_exceptions.Runner({'Владимир': 1995}, 5)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для name объекта Runner", exc_info=True)

        for i in range(10):
            rt_with_exceptions.Runner.run(test_runner)
        self.assertEqual(test_runner.distance, 100)

    @unittest.skipIf(is_frozen, 'Tests in this case are frozen')
    def test_challenge(self):
        test_runner_1 = rt_with_exceptions.Runner('test_runner_1')
        test_runner_2 = rt_with_exceptions.Runner('test_runner_2')
        for i in range(10):
            rt_with_exceptions.Runner.run(test_runner_1)
            rt_with_exceptions.Runner.walk(test_runner_2)
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s ~ %(levelname)s ~ %(message)s")
