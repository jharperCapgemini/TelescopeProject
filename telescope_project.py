import math


class Antenna:
    def __init__(self, x, y):
        # set of coordinates for this specific antenna
        self.coordinates = [x, y]


class Telescope:
    def __init__(self, antenna_list, altitude, azimuth, wavelength):
        # Values for the antennae we're measuring
        self.first_antenna = antenna_list[0]
        self.second_antenna = antenna_list[1]

        # differences between the x and y coordinates for the antennae
        self.x_diff = abs(self.first_antenna[0]-self.second_antenna[0])
        self.y_diff = abs(self.first_antenna[1]-self.second_antenna[1])

        # working out the baseline angle between the antennae as well as the distance between them
        self.baseline_angle = math.atan(self.x_diff/self.y_diff)
        self.distance = math.sqrt(self.x_diff**2 + self.y_diff**2)

        # storing the values of the wave
        self.altitude = altitude
        self.azimuth = azimuth
        self.wavelength = wavelength

    def phase_difference(self):
        # Function which when given the distance, the direction to the source, relative to the baseline
        # and the wavelength and returns the phase difference

        # Path difference
        path_diff = self.distance * round(math.cos(self.altitude))*round(math.cos(self.azimuth - self.baseline_angle))

        # Phase difference
        phase_diff = abs((2*math.pi*path_diff)/self.wavelength)
        # Need to make sure the result is in terms of radians (once reaches 2pi it loops round to 0)
        if phase_diff >= 2*math.pi:
            phase_diff = (2 * math.pi) % abs(((2*math.pi*path_diff)/self.wavelength))
        print(phase_diff)
        return phase_diff


antenna1 = Antenna(1, 1)
antenna2 = Antenna(4, 5)

object = Telescope(antenna_list=[antenna1.coordinates, antenna2.coordinates], altitude=0, azimuth=math.pi, wavelength=200)

object.phase_difference()