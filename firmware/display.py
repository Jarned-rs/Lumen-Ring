import board
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306Driver

display = Display(
    display = SSD1306Driver(i2c = board.I2C(), device_address = 0x3C, width = 128, height = 32),
        entries = [
            TextEntry(text = 'EVENTS',        x=0, y=5,  x_anchor='L', y_anchor='M'),
            TextEntry(text = '2nd Nov - Economics',   x=0, y=16, x_anchor='L', y_anchor='M'),
            TextEntry(text = '3rd Nov - Comp Sci',x=0, y=27, x_anchor='L', y_anchor='M'),
        ]
)

keyboard.extensions.append(display)