from webbrowser import Error

from rt_with_exceptions import Runner, Tournament
import unittest
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_walk_value = Runner('test_walk_value', -5)
            for i in range(10):
                test_walk_value.walk()

            self.assertEqual(test_walk_value.distance, 50)
            logging.info(f'test_walk выполнен успешно')
        except ValueError:
            logging.warning(f'Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_run_value = Runner(8)
            for i in range(10):
                test_run_value.run()
            self.assertEqual(test_run_value.distance, 100)
            logging.info(f'test_run выполнен успешно')
        except TypeError:
            logging.warning(f'Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test_walk_value = Runner('test_walk_value')
        test_run_value = Runner('test_run_value')
        for i in range(10):
            test_walk_value.walk()
            test_run_value.run()
        self.assertNotEqual(test_walk_value.distance, test_run_value.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.useyn = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)


    @classmethod
    def tearDownClass(cls):
        for item, value in cls.all_results.items():
            print()
            print('Тест:', item)
            for k, v in value.items():
                print(k, v)


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_1(self):
        run_1 = Tournament(90, self.useyn, self.nik)
        result = run_1.start()

        self.all_results['test_start_1'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник', 'Тест 1. Ошибка, последним должен быть Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_2(self):
        run_2 = Tournament(90, self.andrey, self.nik)
        result = run_2.start()
        self.all_results['test_start_2'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник', 'Тест 2. Ошибка, последним должен быть Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_3(self):
        run_3 = Tournament(90, self.andrey, self.useyn, self.nik)
        result = run_3.start()
        self.all_results['test_start_3'] = result
        self.assertTrue(result[max(result.keys())] == 'Ник', 'Тест 3. Ошибка, последним должен быть Ник')

logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_test.log',
                        encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':

    # logging.basicConfig(level=logging.INFO,
    #                     filemode='w',
    #                     filename='runner_test.log',
    #                     encoding='utf-8',
    #                     format='%(asctime)s | %(levelname)s | %(message)s')

    unittest.main()