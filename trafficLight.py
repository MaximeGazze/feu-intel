from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory


class TrafficLight:
    def __init__(self, red_led_pin: int, yellow_led_pin: int, green_led_pin: int):
        """
        A collection of three LEDs (red, yellow and green) used as a traffic light.

        :param red_led_pin: The red LED pin
        :param yellow_led_pin: The yellow LED pin
        :param green_led_pin: The green LED pin
        """
        self.state = 'off'
        self.red_led = LED(red_led_pin, pin_factory=PiGPIOFactory())
        self.yellow_led = LED(yellow_led_pin, pin_factory=PiGPIOFactory())
        self.green_led = LED(green_led_pin, pin_factory=PiGPIOFactory())
        self.identifier = None
        self.intersection = None

    def red(self) -> None:
        """Change traffic light to red"""
        self.red_led.on()
        self.yellow_led.off()
        self.green_led.off()
        self.state = 'red'

    def yellow(self) -> None:
        """Change traffic light to yellow"""
        self.red_led.off()
        self.yellow_led.on()
        self.green_led.off()
        self.state = 'yellow'

    def green(self) -> None:
        """Change traffic light to green"""
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.on()
        self.state = 'green'

    def all(self) -> None:
        """Change traffic light to green"""
        self.red_led.on()
        self.yellow_led.on()
        self.green_led.on()
        self.state = 'off'

    def off(self) -> None:
        """Change traffic light to off"""
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.off()
        self.state = 'off'
    
    def lightsStates(self):
        return self.state    
