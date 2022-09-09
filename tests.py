import unittest

from telescope_project import Antenna
from telescope_project import Telescope


class BasicTelescopeTests(unittest.TestCase):

    def test_standard_baseline_vector(self):
        antenna1 = Antenna(1, 1)
        antenna2 = Antenna(4, 5)
        test_telescope = Telescope(antenna_list=[antenna1.coordinates, antenna2.coordinates], altitude=0, azimuth=0, wavelength=200)
        self.assertEqual(test_telescope.distance, 5)

    def test_negative_baseline_vector(self):
        antenna3 = Antenna(5, 4)
        antenna4 = Antenna(1, 1)
        test2_telescope = Telescope(antenna_list=[antenna3.coordinates, antenna4.coordinates], altitude=0, azimuth=0, wavelength=200)
        self.assertEqual(test2_telescope.distance, 5)

if __name__ == '__main__':
    unittest.main()
