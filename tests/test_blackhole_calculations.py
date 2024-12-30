import unittest
from blackhole_calculations import calculate_schwarzschild_radius, calculate_event_horizon, calculate_hawking_radiation

class TestBlackholeCalculations(unittest.TestCase):

    def test_calculate_schwarzschild_radius(self):
        mass = 1.989e30  # mass of the sun in kg
        expected_radius = 2.95325008e3  # expected Schwarzschild radius in meters
        self.assertAlmostEqual(calculate_schwarzschild_radius(mass), expected_radius, places=5)

    def test_calculate_event_horizon(self):
        mass = 1.989e30  # mass of the sun in kg
        expected_horizon = 2.95325008e3  # expected event horizon in meters
        self.assertAlmostEqual(calculate_event_horizon(mass), expected_horizon, places=5)

    def test_calculate_hawking_radiation(self):
        mass = 1.989e30  # mass of the sun in kg
        expected_radiation = 9.098e-29  # expected Hawking radiation in watts
        self.assertAlmostEqual(calculate_hawking_radiation(mass), expected_radiation, places=33)

if __name__ == '__main__':
    unittest.main()
