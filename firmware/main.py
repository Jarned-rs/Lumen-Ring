import time
import board
import usb_cdc

from digitalio import DigitalInOut, Direction
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules import Module
from kmk.modules.encoder import EncoderHandler

total_leds = 20

pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP7,
)

led_pairs = [
    (0, 1), (0, 2), (0, 3), (0, 4),
    (1, 0), (1, 2), (1, 3), (1, 4),
    (2, 3), (2, 4), (2, 0), (2, 1),
    (3, 4), (3, 0), (3, 1), (3, 2),
    (4, 0), (4, 1), (4, 2), (4, 3),
]

led_pins = [DigitalInOut(pin) for pin in pins]

yellow = range(0, 6)
orange = range(6, 13)
red = range(13, 20)


LED_INTERVAL = 0.0005

display_leds = []
current_led = 0
last_refresh = time.monotonic()


def turn_on_led(led_number):

    for pin in led_pins:
        pin.direction = Direction.INPUT
    positive, negative = led_pairs[led_number]
    led_pins[negative].direction = Direction.OUTPUT
    led_pins[negative].value = False
    led_pins[positive].direction = Direction.OUTPUT
    led_pins[positive].value = True


def calculate_active_leds(volume_percent):
    return round((volume_percent / 100) * total_leds)


def get_active_leds(active_leds):
    return list(range(active_leds))


def update_display(volume_percent):
    global display_leds
    global current_led
    active_count = calculate_active_leds(volume_percent)
    display_leds = get_active_leds(active_count)
    current_led = 0


def refresh_leds():
    global current_led
    global last_refresh
    current_time = time.monotonic()
    if current_time - last_refresh >= LED_INTERVAL:
        last_refresh = current_time
        if display_leds:
            turn_on_led(display_leds[current_led])
            current_led = (current_led + 1) % len(display_leds)
        else:
            for pin in led_pins:
                pin.direction = Direction.INPUT

serial_port = usb_cdc.data
serial_buffer = bytearray()

def receive_volume():
    if serial_port.in_waiting:
        incoming = serial_port.read(serial_port.in_waiting)
        serial_buffer.extend(incoming)
    while b"\n" in serial_buffer:
        newline_index = serial_buffer.index(b"\n")
        message = bytes(serial_buffer[:newline_index])
        del serial_buffer[:newline_index + 1]
        volume_percent = int(message.decode("ascii").strip())
        if 0 <= volume_percent <= 100:
            update_display(volume_percent)


class VolumeSerialModule(Module):

    def before_matrix_scan(self, keyboard):
        receive_volume()
        refresh_leds()


keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP6, board.GP5, board.GP4, False),
)
encoder_handler.map = [
    (KC.VOLD, KC.VOLU, KC.MUTE)
]
keyboard.modules = [
    encoder_handler,
    VolumeSerialModule()
]


if __name__ == "__main__":
    keyboard.go()
