# Lumen-Ring

The lumen ring is a simple project designed to teach myself about charlieplexing and how it works in real situations. It reacts on the volume that your PC is set to and has a OLED to show upcoming events for you that can be changed easily in the code.

# Features
- RP2040-Zero to control the LEDS and OLED
- OLED to display your upcoming events
- 20 LEDS charlieplexed in 5pin with 3 colours to correspond with your PC's volume
- A rotary encoder to turn your volume up, down and mute sound
- A case with a hinge to keep the LEDs and OLED safe during storage! 

# How it works
On a basic GPIO port, we have 2 main modes that they can be in, either HIGH or LOW. Charlieplexing uses a 3rd mode called INPUT to fit more LEDS on one pin.
- A script reads the volume and sends it via USB to the 2040
- The 2040 reads the volume and decides how many LEDS need to be switched on
- It finds the right LEDs and turns them on

# Photos
Case:
<img width="1734" height="1087" alt="image" src="https://github.com/user-attachments/assets/3e24c82c-5935-48ac-8b14-49a1d19b2c40" />

