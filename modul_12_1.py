from unittest import TestCase
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0
    def run(self):
        self.distance += 10
    def walk(self):
        self.distance += 5
    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk (self):
        rur = Runner ('Li-Li')
        for i in range(10):
            rur.walk()
        self.assertEqual(rur.distance ,50)
    def test_run (self):
        rur = Runner ('Li-Li')
        for i in range(10):
            rur.run()
        self.assertEqual(rur.distance ,100)
    def test_challenge(self):
        rur_k = Runner("Kri-Kri")
        rur_s = Runner("Si-Si")
        for i in range(10):
            rur_k .run()
            rur_s .walk()
        self.assertNotEqual(rur_k .distance, rur_s.distance)

