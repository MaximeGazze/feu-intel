from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory

class TrafficLight:
    def __init__(self, red_led_pin: int, yellow_led_pin: int, green_led_pin: int):
        self.state = None
        self.red_led = LED(red_led_pin, pin_factory=PiGPIOFactory())
        self.yellow_led = LED(yellow_led_pin, pin_factory=PiGPIOFactory())
        self.green_led = LED(green_led_pin, pin_factory=PiGPIOFactory())
        self.intersection: Intersection = None

    def red(self):
        self.red_led.on()
        self.yellow_led.off()
        self.green_led.off()
        self.state = 'r'

    def yellow(self):
        self.red_led.off()
        self.yellow_led.on()
        self.green_led.off()
        self.state = 'y'

    def green(self):
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.on()
        self.state = 'g'

    def off(self):
        self.red_led.off()
        self.yellow_led.off()
        self.green_led.off()
        self.state = None
