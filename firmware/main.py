import board
from kmk.kmk_keyboard import KMKKKeyboard
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#Chalieplexing
total_leds = 20
pins = (
    board.GP0
    board.GP1
    board.GP2
    board.GP3
    board.GP7
)




#encoder setup
encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]
encoder_handler.pins = (
    (board.GP6, board.GP5, board.GP4, False)
)
encoder_handler.map = [((KC.VOLD, KC.VOLU, KC.MUTE))]


#getting volume using pycaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

current_vol_scalar = volume.GetMasterVolumeLevelScalar()
current_vol_percent = current_vol_scalar * 100