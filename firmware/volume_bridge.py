import time
import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilitie.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_,
    CLSCTX_ALL,
    None
)

volume = cast(interface, POINTER(IAudioEndpointVolume))

pico = serial.Serial("COMS", 115200, timeout = 0)

try:
    while True:
        volume_percent = round(
            volume.GetMasterVolumeLevelScalar() * 100
        )
        message = f"{volume_percent}\n"
        pico.write(message.encode("ascii"))
        time.sleep(0.1
        )

finally:
    pico.close()