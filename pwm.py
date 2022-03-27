from __future__ import annotations

from pyb import Timer
from machine import Pin


__author__ = "Nikolay Putko"
__copyright__ = "Nikolay Putko, 2022 onwards."
__license__ = "MIT https://opensource.org/licenses/MIT (as used by MicroPython)."
__version__ = "1.0.0"  # Version set by https://github.com/hlovatt/tag2ver

class PWM:
    pin = None
    freq = None
    width = None
    cnl = None
    t = None
    p = None

    pin_dict = {'A0': (2, 1),
                'A1': (2, 2),
                'A2': (2, 3),
                'A3': (2, 4),
                'A5': (2, 1),
                'LED1': (4, 1),
                'LED2': (4, 2),
                'P0': (2, 4),
                'P1': (2, 3),
                'P2': (3, 1),
                'P3': (3, 2),
                'P5': (3, 4),
                'P6': (3, 3),
                'P8': (3, 1),
                'P9': (3, 2),
                'SCL': (4, 3),
                'SDA': (4, 4),
                }

    def __init__(self, p: str, freq=500, width=255):
        self.pin = p
        self.freq = freq
        self.width = width

        if p not in self.pin_dict.keys():
            raise ValueError(p + ' Pin is not allowed for PWM on Iskra board')
        self.p = Pin(p, Pin.OUT)
        self.t = Timer(self.pin_dict[p][0], freq=freq)
        self.cnl = self.t.channel(self.pin_dict[p][1], Timer.PWM, pin=self.p)
        self.cnl.pulse_width(width)

    def duty(self, percent: int | float, /) -> None:
        if percent < 0:
            percent = 0
        if percent > 100:
            percent = 100
        self.cnl.pulse_width_percent(percent)

    def value(self, percent):
        self.duty(percent)
