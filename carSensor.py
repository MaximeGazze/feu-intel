from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory


class CarSensor(DistanceSensor):
    def __init__(self, echo_pin: int, trig_pin: int):
        """
        Represents a distance sensor connected via GPIO used to sense if a car is present or not.

        This class extends :class:`DistanceSensor` to utilise the gpiozero package functionality and
        set smart defaults to optimize the tracking.

        :param echo_pin: The GPIO pin used for echo.
        :param trig_pin: The GPIO pin used for trigger.
        """
        DistanceSensor.__init__(
            self,
            echo_pin,
            trig_pin,
            max_distance=1,
            pin_factory=PiGPIOFactory(),
            threshold_distance=0.2
        )
        self.direction = None
        self.intersection = None
        self.when_in_range = self.__when_in_range

    def __when_in_range(self) -> None:
        """Call the associated intersection's update method when a car is detected in the threshold distance."""
        self.intersection.update(self)
